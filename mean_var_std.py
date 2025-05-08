import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(list).reshape(3, 3)
    
    calculations = {
        'mean': [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), np.mean(arr)],
        'variance': [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), np.var(arr)],
        'standard deviation': [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), np.std(arr)],
        'max': [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), np.max(arr)],
        'min': [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), np.min(arr)],
        'sum': [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), np.sum(arr)]
    }
    
    return calculations

