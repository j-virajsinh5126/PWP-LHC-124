import numpy as np
import matplotlib.pyplot as plt
from signal_ICT_Virajsinh_124 import unitary as u
from signal_ICT_Virajsinh_124 import trignometric as tr
from signal_ICT_Virajsinh_124 import operations as oprs

if __name__ == "__main__":
    n = np.arange(-10, 11)  # Range from -10 to 10
    print("Unit Step:", u.unit_step(n))
    print("Unit Impulse:", u.unit_impulse(n))
    print("Ramp:", u.ramp_signal(n))

# Example usage (runs only if file executed directly)
if __name__ == "__main__":
    t = np.linspace(0, 1, 500)  # time from 0 to 1 sec with 500 samples
    tr.sine_wave(1, 5, 0, t)       # Sine wave: A=1, f=5Hz, phi=0
    tr.cosine_wave(1, 5, 0, t)     # Cosine wave: A=1, f=5Hz, phi=0
    tr.exponential_signal(1, -2, t)  # Exponential decay
    
# Example usage
if __name__ == "__main__":
    n = np.arange(-5, 6)
    signal1 = np.where(n >= 0, 1, 0)  # unit step
    signal2 = np.where(n == 0, 1, 0)  # unit impulse

    # Time shift
    oprs.time_shift(signal1, n, 2)

    # Time scaling
    oprs.time_scale(signal1, n, 2)

    # Addition
    oprs.signal_addition(signal1, signal2)

    # Multiplication
    oprs.signal_multiplication(signal1, signal2)