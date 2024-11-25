from moviepy.editor import VideoFileClip

def extract_audio(video_path, output_audio_path):
    try:
        # Carrega o arquivo de vídeo
        video = VideoFileClip(video_path)
        
        # Extrai o áudio
        audio = video.audio
        
        # Salva o áudio em um arquivo .mp3
        audio.write_audiofile(output_audio_path)
        
        # Libera os recursos
        audio.close()
        video.close()
        print(f"Áudio extraído com sucesso e salvo em: {output_audio_path}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Caminhos dos arquivos
video_file = "video.mp4"
output_audio_file = "audio.mp3"

# Chama a função
extract_audio(video_file, output_audio_file)