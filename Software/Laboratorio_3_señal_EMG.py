import numpy as np
import matplotlib.pyplot as plt
fs = 1000
ts = 1/fs
data = np.genfromtxt("señal_emg.txt", skip_header=3)
print(data)
signal = data[:, -1]
signal = signal*3.3/1023
t = np.arange(0, len(signal))*ts
plt.plot(t, signal)
plt.xlabel("tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.title("Grafica de señal EMG del bíceps")
plt.grid()
plt.show()
