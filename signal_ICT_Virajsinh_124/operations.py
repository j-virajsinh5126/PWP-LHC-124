import numpy as np
import matplotlib.pyplot as plt


def time_shift(signal, n, k):

    shifted_n = n + k
    shifted_signal = signal
    plt.stem(shifted_n, shifted_signal, basefmt=" ")
    plt.title(f"Time Shifted Signal (k={k})")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return shifted_n, shifted_signal


def time_scale(signal, n, k):

    scaled_n = n * k
    scaled_signal = signal
    plt.stem(scaled_n, scaled_signal, basefmt=" ")
    plt.title(f"Time Scaled Signal (k={k})")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return scaled_n, scaled_signal


def signal_addition(signal1, signal2):
   
    if len(signal1) != len(signal2):
        raise ValueError("Signals must be of same length for addition.")
    added_signal = signal1 + signal2
    plt.stem(range(len(added_signal)), added_signal, basefmt=" ")
    plt.title("Signal Addition")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return added_signal


def signal_multiplication(signal1, signal2):

    if len(signal1) != len(signal2):
        raise ValueError("Signals must be of same length for multiplication.")
    multiplied_signal = signal1 * signal2
    plt.stem(range(len(multiplied_signal)), multiplied_signal, basefmt=" ")
    plt.title("Signal Multiplication")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return multiplied_signal



