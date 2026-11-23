import numpy as np

def make_hours() -> list[int]:
    arr = np.arange(0, 22, 3)
    
    return arr.tolist()

def vector_report(values: list[float]) -> dict:
    arr = np.array(values)
    third = arr[2]
    last = arr[-1]
    middle = arr[2:6]
    every_second = arr[::2]
    reversed = arr[::-1]
    
    return {
        "third": float(third),
        "last": float(last),
        "middle": middle.tolist(),
        "every_second": every_second.tolist(),
        "reversed": reversed.tolist()
    }

def change_vector(values: list[float]) -> list[float]:
    arr = np.array(values, dtype=float).copy()
    arr[2:5] = 99.0
    arr[::2] = -1.0
    
    return arr.tolist()

def cap_above(values: list[float], limit: float) -> list[float]:
    arr = np.array(values).copy()
    mask = arr > limit
    arr[mask] = limit
    
    return arr.tolist()

def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    arr = np.array(values)
    fahrenheit  = arr * 9 / 5 + 32
    
    return fahrenheit.tolist()