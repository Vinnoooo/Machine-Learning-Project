import numpy as np
import matplotlib.pyplot as plt

# 1. Create a signal: sum of two sine waves
t = np.linspace(0, 1, 1000)  # 1 second, 1000 samples
f1, f2 = 5, 20               # frequencies in Hz
signal = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

# 2. Compute FFT
F = np.fft.fft(signal)
freq = np.fft.fftfreq(len(signal), d=(t[1]-t[0]))

# --- First figure: FFT Magnitude Spectrum ---
mask = freq >= 0
plt.figure(figsize=(10,4))
plt.plot(freq[mask], np.abs(F[mask]))
plt.title("FFT Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("|F(ω)|")
plt.grid(True)

# --- Second figure: Original vs Filtered Signal ---
fft_coeffs = np.fft.fft(signal)
fft_coeffs[10:-10] = 0           # zero out high-frequency components
filtered_signal = np.fft.ifft(fft_coeffs)

plt.figure(figsize=(10,4))        # Create a new figure for the second plot
plt.plot(t, signal, label='Original')
plt.plot(t, filtered_signal.real, label='Filtered')
plt.title("Original vs Filtered Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Show both figures at the same time
plt.show()


