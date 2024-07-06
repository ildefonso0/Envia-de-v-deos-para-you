import requests
from bs4 import BeautifulSoup
from io import BytesIO
from auth import authenticate_drive
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)

def get_video_links(playlist_url):
    response = requests.get(playlist_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    video_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if 'watch' in href:
            video_links.append('https://www.youtube.com' + href)
    return video_links

def create_folder(drive, folder_name):
    folder_metadata = {'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
    return folder['id']

def upload_video(drive, video_url, title, folder_id):
    try:
        response = requests.get(video_url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        video_content = BytesIO(response.content)
        
        upload_file = drive.CreateFile({'title': title, 'parents': [{'id': folder_id}]})
        upload_file.SetContentFile(video_content)
        upload_file.Upload()
        
        logging.info('Upload concluído! Link do arquivo: %s', upload_file['alternateLink'])
    except requests.exceptions.RequestException as e:
        logging.error('Erro ao baixar o vídeo: %s', e)
    except Exception as e:
        logging.error('Erro ao fazer o upload: %s', e)

def upload_playlist(playlist_url):
    drive = authenticate_drive()
    video_links = get_video_links(playlist_url)
    playlist_name = "Nome_da_Playlist"  # Substitua pelo nome real da playlist
    folder_id = create_folder(drive, playlist_name)
    
    for i, video_url in enumerate(video_links):
        title = f'video_{i+1}.mp4'
        upload_video(drive, video_url, title, folder_id)

if __name__ == '__main__':
    load_dotenv()
    playlist_url = os.getenv('PLAYLIST_URL')
    upload_playlist(playlist_url)
