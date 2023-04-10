from gtts import gTTS
import os
from pygame import mixer, time

def main(text, file_name):
    try:
        audio = gTTS(text=text, slow=False)
        audio.speed = 1.1
        audio.save(f"{file_name}.mp3")
        
        mixer.init()
        mixer.music.load(f"{file_name}.mp3")
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(10)

        # Clean up
        mixer.quit()
        os.remove(f"{file_name}.mp3")
    except Exception as error:
        print(error)
