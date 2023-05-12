import pyaudio
import webrtcvad
import serial

ser = serial.Serial('COM5', 9600)

# Set up PyAudio
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
CHUNK_DURATION_MS = 30  # in ms
CHUNK_SIZE = int(RATE * CHUNK_DURATION_MS / 1000)  # in samples
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK_SIZE)

# Set up VAD
vad = webrtcvad.Vad()
vad.set_mode(3)  # Aggressive mode

# Loop to read audio from microphone and perform VAD
while True:
    # Read audio from microphone
    audio = stream.read(CHUNK_SIZE)

    # Perform VAD
    is_speech = vad.is_speech(audio, RATE)
    if is_speech:
        # Do something when speech is detected
        # print("Speech detected!")
        ser.write(b'1')
    else:
        # Do something when no speech is detected
        # print("No speech detected.")
        ser.write(b'0')
ser.close()