import numpy as np

def make_hours() -> list[int]:
    arr = np.arrange(0, 22, 3)
    
    return arr.tolist()

def vector_report(values: list[float]) -> dict:
    arr = np.array(values)
    third = arr[2]
    last = arr[-1]
    middle = arr[2:6]
    every_second = [::2]
    reversed = arr[::-1]
    
    return {
        "third": float(third),
        "last": float(last),
        "middle": middle.tolist(),
        "every_second": every_second.tolist(),
        "reversed": reversed.tolist()
    }

def change_vector(values: list[float]) -> list[float]
    arr = np.array(values).copy()
    arr[2:5] = 99
    arr[1::2] = -1
    
    return arr.tolist()