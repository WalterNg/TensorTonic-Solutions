import numpy as np
import math

def sigmoid(X: float | np.ndarray) -> np.ndarray:
    """
    Vectorized sigmoid function.
    """
    X = np.asarray(X, dtype=float)
    return 1 / (1 + math.e**(-X))
        