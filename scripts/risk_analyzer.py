import numpy as np

def calculate_var(returns, confidence_level):
    return -np.percentile(returns, (1 - confidence_level) * 100)