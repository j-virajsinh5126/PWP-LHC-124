#trignometric_signals
import numpy as np 
import matplotlib.pyplot as plt

#Function to generate SINE WAVE 
def sine_wave(A, f, phi, t):
    y = A * np.sin(2 * np.pi * f * t + phi)
    plt.plot(t, y)
    plt.title("---SINE WAVE---")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return y

#Function to genereate COSINE WAVE
def cosine_wave(A, f, phi, t):
    y = A * np.cos(2 * np.pi * f * t + phi)
    plt.plot(t, y)
    plt.title("---COSINE WAVE---")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return y

#Function to generate EXPOPNENTIAL SIGNAL
def exponential_signal(A, a, t):
    y = A * np.exp(a * t)
    plt.plot(t, y)
    plt.title("---EXPONENTIAL SIGNAL---")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return y

