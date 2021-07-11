import numpy as np

def get_circle_area(r):

    if r < 0:
        raise ValueError("The radius cannot be negative.")
    
    return np.pi * np.power(r, 2)