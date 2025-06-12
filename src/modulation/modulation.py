import numpy as np
def bpsk_modulate(bits):
    return np.array([1 if b else -1 for b in bits], dtype=float)
def bpsk_demodulate(symbols):
    return [1 if s > 0 else 0 for s in symbols]
