from gtts import gTTS
import os

def main(text, file_name):
    try:
        audio = gTTS(text=text, slow=False)
        audio.speed = 1.1
        audio.save(f"{file_name}.mp3")
        os.system(f"cvlc {file_name}.mp3 --play-and-exit")
    except Exception as error:
        print(error)
