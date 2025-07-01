import sounddevice as sou
from scipy.io.wavfile import write

fs=44100 
seconds=10
print("recording...")

record_voice=sou.rec(int(seconds * fs),samplerate=fs,channels=2)
sou.wait()

write("out.wav",fs,record_voice)