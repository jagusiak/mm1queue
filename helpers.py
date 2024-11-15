import numpy as np


def random_service_time(rate: float) -> float:
    # generate with exponential distribution,
    # simulates incoming requests in m/m/1 queue
    return np.random.exponential(1 / rate)
