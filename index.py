from moviepy.editor import VideoFileClip
import speech_recognition as sr
import os

def extract_audio(video_file, output_audio_file):
    """Extrai o áudio de um arquivo de vídeo e o salva como .wav"""
    print("Extraindo o áudio do vídeo...")
    video = VideoFileClip(video_file)
    video.audio.write_audiofile(output_audio_file)
    print(f"Áudio salvo em: {output_audio_file}")

def transcribe_audio(audio_file):
    """Transcreve o áudio usando SpeechRecognition"""
    print("Transcrevendo o áudio...")
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="en-US")
            print("Transcrição concluída!")
            return text
        except sr.UnknownValueError:
            return "Não foi possível entender o áudio."
        except sr.RequestError as e:
            return f"Erro na API de reconhecimento de fala: {e}"

def main():
    video_file = "video.mp4"  # Substitua pelo caminho do seu vídeo
    audio_file = "audio.wav"

    # Extrair o áudio do vídeo
    extract_audio(video_file, audio_file)

    # Transcrever o áudio
    transcription = transcribe_audio(audio_file)
    print("\nTranscrição do áudio:")
    print(transcription)

    # Remover o arquivo de áudio temporário
    os.remove(audio_file)

if __name__ == "__main__":
    main()