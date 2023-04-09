import pyaudio
import wave
import keyboard

# Set the audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 8192 # increase buffer size
WAVE_OUTPUT_FILENAME = "output.wav"

# Initialize the PyAudio object
audio = pyaudio.PyAudio()

# Open the audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Press 's' to start recording and 'q' to quit...")

frames = []
while True:
    if keyboard.is_pressed('s'):
        print("Recording...")
        break

while True:
    if keyboard.is_pressed('q'):
        print("Recording stopped.")
        break
    try:
        data = stream.read(CHUNK)
    except OSError as ex:
        if ex.errno == -9981:
            continue
        else:
            raise
    frames.append(data)

# Stop the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a WAV file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
