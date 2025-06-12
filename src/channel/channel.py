import numpy as np
def awgn_channel(symbols, snr_db):
    power = np.mean(symbols**2)
    snr = 10**(snr_db/10)
    noise_power = power / snr
    noise = np.sqrt(noise_power) * np.random.randn(len(symbols))
    return symbols + noise
