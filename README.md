# Envia-de-v-deos-para-you
Não faça m+rda🖇️🇦🇴🔧

# Playlist Upload to Drive

Este projeto faz o upload de todos os vídeos de uma playlist diretamente para o Google Drive, criando uma pasta com o nome da playlist.

## Estrutura do Projeto

- `requirements.txt`: Dependências do projeto.
- `auth.py`: Autenticação no Google Drive.
- `upload_playlist.py`: Script para fazer o upload dos vídeos da playlist.
- `.env`: Arquivo de configuração com a URL da playlist.

## Configuração

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/playlist-upload-to-drive.git
cd playlist-upload-to-drive

Crie um arquivo .env e adicione a URL da playlist:
PLAYLIST_URL=https://example.com/playlist

Instale as dependências:
pip install -r requirements.txt

Execução
python upload_playlist.py

Licença
[Nome da licença]


### Passos no Google Colab

1. **Abra o Google Colab** e crie um novo notebook.
2. **Clone o repositório do GitHub** no Google Colab:

```python
!git clone https://github.com/SEU_USUARIO/playlist-upload-to-drive.git
%cd playlist-upload-to-drive

Instale as dependências listadas no requirements.txt:
Python

!pip install -r requirements.txt
Código gerado por IA. Reveja e utilize cuidadosamente. Mais informações sobre as FAQ.
Execute o script upload_playlist.py:
Python

!python upload_playlist.py
Código gerado por IA. Reveja e utilize cuidadosamente. Mais informações sobre as FAQ.
Certifique-se de substituir 'URL_DA_PLAYLIST' pelo link real da playlist que você deseja fazer o upload no arquivo .env.
