from gtts import gTTS
import os

def main(text, file_name):
    audio = gTTS(text=text, slow=False)
    audio.speed = 1.1
    audio.save(f"{file_name}.mp3")
    os.system(f"open {file_name}.mp3")
