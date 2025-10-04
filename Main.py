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

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)
signal = np.sin(2*np.pi*t) + 0.5*np.sin(50*np.pi*t)

# Fourier transform
fft_coeffs = np.fft.fft(signal)
# Zero out high-frequency coefficients
fft_coeffs[10:-10] = 0
# Reconstruct signal
filtered_signal = np.fft.ifft(fft_coeffs)

plt.plot(t, signal, label='Original')
plt.plot(t, filtered_signal.real, label='Filtered')
plt.legend()
plt.show()

"Tada!"