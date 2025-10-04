import numpy as np
import matplotlib.pyplot as plt

# 1. Create a signal: sum of two sine waves
t = np.linspace(0, 1, 1000)  # 1 second, 1000 samples
f1, f2 = 5, 20               # frequencies in Hz
signal = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

# 2. Compute FFT
F = np.fft.fft(signal)
freq = np.fft.fftfreq(len(signal), d=(t[1]-t[0]))

# 3. Take only the positive frequencies for plotting
mask = freq >= 0
plt.figure(figsize=(10,4))
plt.plot(freq[mask], np.abs(F[mask]))
plt.title("FFT Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("|F(ω)|")
plt.grid(True)
plt.show()
