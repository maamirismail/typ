from itertools import combinations

def median3(values):
    """
    median of 3 values using standard 3 comparator network
    returns the median and the number of comparisons made
    """
    a = list(values)
    comparisons = 0
    for i, j in [(0, 1), (1, 2), (0, 1)]:
        comparisons += 1
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
    return a[1], comparisons