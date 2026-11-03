from itertools import combinations

def median3(values):
    """
    median of 3 values 
    """
    a = list(values)
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
    return a[1]