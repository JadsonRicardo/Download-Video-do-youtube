#Importar o módulo "PYtube"
from pytube import YouTube, streams
from pytube.cli import on_progress

#Inserir o url do vídeo
link = input ('Insira aqui o seu link: ')

yt = YouTube(link, on_progress_callback = on_progress)

print('Titulo = ', yt.title)

print('Baixando...')

#Para baixar a melhor resolução do viídeo
ys = yt.streams.get_highest_resolution()
ys.download()
