import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Sampling parameters
fs = 1000  # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # 1 second of data

# Generate clean sine wave signal (50 Hz)
clean_signal = np.sin(2 * np.pi * 50 * t)

# Add random noise
noise = np.random.normal(0, 0.5, size=t.shape)

# Add EMI (150 Hz interference)
emi = 0.7 * np.sin(2 * np.pi * 150 * t)

# Combine clean signal, noise, and EMI
noisy_signal = clean_signal + noise + emi

# Plot the raw noisy signal
plt.figure(figsize=(12, 6))
plt.plot(t, noisy_signal, label="Noisy Signal", color="red", alpha=0.7)
plt.plot(t, clean_signal, label="Clean Signal (50 Hz)", linestyle="--", color="blue")
plt.title("Clean and Noisy Signals")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()

# Low-pass filter design
def butter_lowpass(cutoff, fs, order=4):
    nyquist = 0.5 * fs  # Nyquist frequency
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

# Band-stop filter design
def butter_bandstop(lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='bandstop', analog=False)
    return b, a

# Apply low-pass filter (cutoff at 100 Hz)
b, a = butter_lowpass(100, fs)  # Allow frequencies below 100 Hz
filtered_signal_lowpass = filtfilt(b, a, noisy_signal)

# Apply band-stop filter (stopband: 145-155 Hz)
b, a = butter_bandstop(145, 155, fs)
filtered_signal_bandstop = filtfilt(b, a, noisy_signal)

# Plot the filtered signals
plt.figure(figsize=(12, 6))
plt.plot(t, noisy_signal, label="Noisy Signal", color="red", alpha=0.5)
plt.plot(t, filtered_signal_lowpass, label="Low-Pass Filtered Signal", color="green", linewidth=2, linestyle="--")
plt.plot(t, filtered_signal_bandstop, label="Band-Stop Filtered Signal", color="blue", linewidth=2)
plt.title("Filtered Signals")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()

# Perform frequency spectrum analysis
frequencies = np.fft.fftfreq(len(t), 1/fs)

# Fourier Transform of the noisy signal
fft_noisy_signal = np.fft.fft(noisy_signal)

# Fourier Transform of the low-pass filtered signal
fft_filtered_lowpass = np.fft.fft(filtered_signal_lowpass)

# Plot frequency spectrum
plt.figure(figsize=(12, 6))
plt.plot(frequencies[:fs//2], np.abs(fft_noisy_signal)[:fs//2], label="Noisy Signal Spectrum", color="red")
plt.plot(frequencies[:fs//2], np.abs(fft_filtered_lowpass)[:fs//2], label="Low-Pass Filtered Spectrum", color="green")
plt.title("Frequency Spectrum Analysis")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
