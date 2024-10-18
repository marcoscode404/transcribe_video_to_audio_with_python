# pip install moviepy SpeechRecognition pydub

from moviepy.editor import VideoFileClip
import speech_recognition as sr

# Código para extrair o áudio do vídeo
# Vamos começar extraindo o áudio de um vídeo com a biblioteca moviepy:
# Esse código pega um arquivo de vídeo, extrai o áudio e o salva como um arquivo separado.
def extract_audio(video_file, audio_output):
    video = VideoFileClip(video_file)
    video.audio.write_audiofile(audio_output)
    print(f"Áudio extraído e salvo em: {audio_output}")


# -------------------------------------
# Transcrever o áudio usando SpeechRecognition
# Agora, vamos utilizar a biblioteca SpeechRecognition para converter o áudio em texto:
def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  # lê o áudio do arquivo

    try:
        # Usando o reconhecimento de fala do Google (online)
        text = recognizer.recognize_google(audio, language="pt-BR")
        print("Transcrição: ", text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition não conseguiu entender o áudio")
    except sr.RequestError as e:
        print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala: {e}")

# --------------------------------------
#  Integrar o sistema
# Podemos agora unir os dois passos para criar o sistema completo. O sistema vai pegar o vídeo, extrair o áudio e depois transcrever o áudio em texto.
def video_to_text(video_file):
    audio_file = "output_audio.wav"
    extract_audio(video_file, audio_file)
    transcription = transcribe_audio(audio_file)
    return transcription

# Exemplo de uso
video_path = "video.mp4"  # coloque o caminho do seu vídeo aqui
texto_transcrito = video_to_text(video_path)
print("Texto transcrito do vídeo: ", texto_transcrito)
