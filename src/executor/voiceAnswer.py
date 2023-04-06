from gtts import gTTS
import os

def main(text):
    audio = gTTS(text=text, slow=False)
    audio.save("NOT_POSSIBLE_ACTION.mp3")
    os.system("open NOT_POSSIBLE_ACTION.mp3")
