import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np

#file = "Good_Sounds/3.wav"
file = "Bad_Sounds/1.wav"

#waveform
#signal = sr * duration t -> 44100 * 7
signal, sr = librosa.load(file, sr = 22050)
count = 0
for element in signal:
    if element == 0:
        count = count + 1000
        signal = signal[0:count]
    count += 1

print(signal)
librosa.display.waveplot(signal, sr = sr)
plt.xlabel("Time")
plt.ylabel ("Amplitude")
plt.show()

#fft -> spectrum
fft = np.fft.fft(signal)

magnitude = np.abs(fft)
frequency = np.linspace(0, sr, len(magnitude))
left_frequency = frequency[:int(len(frequency)/2)]
left_magnitude = magnitude[:int(len(frequency)/2)]

plt.plot(left_frequency, left_magnitude)
plt.xlabel("Frequency")
plt.ylabel ("Magnitude")
plt.show()

#stft -> spectogram

n_fft = 2048
hop_length = 512
stft = librosa.core.stft(signal, hop_length = hop_length, n_fft = n_fft)
spectrogram = np.abs(stft)

log_spectogram = librosa.amplitude_to_db(spectrogram)

librosa.display.specshow(log_spectogram, sr = sr, hop_length = hop_length )
plt.xlabel("Time")
plt.ylabel ("Frequency")
plt.colorbar()
plt.show()

#MFCCs
MFFCs = librosa.feature.mfcc(signal, n_fft = n_fft, hop_length = hop_length,n_mfcc=13)
librosa.display.specshow(MFFCs, sr = sr, hop_length = hop_length )
plt.xlabel("Time")
plt.ylabel ("MFCC")
plt.colorbar()
plt.show()


