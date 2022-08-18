# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
frequency = 44400

# Recording duration in seconds
duration = 3.5

# to record audio from
# sound-device into a Numpy
recording = sd.rec(int(duration * frequency),
				samplerate = frequency, channels = 2)

# Wait for the audio to complete
sd.wait()

# using scipy to save the recording in .wav format
# This will convert the NumPy array
# to an audio file with the given sampling frequency
write("input1.wav", frequency, recording)

# using wavio to save the recording in .wav format
# This will convert the NumPy array to an audio
# file with the given sampling frequency
wv.write("input2.wav", recording, frequency, sampwidth=4)
