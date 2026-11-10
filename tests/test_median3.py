from itertools import product
from selection import median3

def test_median3_all_64_triples():
    """
    Test median3 with all 64 triples of values from the set {0, 1, 2, 3}.
    """
    failures = []
    for x in product(range(4), repeat = 3):
        median, comparisons = median3(x)
        if median != sorted(x)[1]:
            failures.append(x)
    assert not failures, f"Test failed for triples: {failures}"