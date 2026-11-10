# Stage 1 notes

Full working is in `notebooks/stage1.ipynb`, code in `src/`, and tests in `tests/`.

## Environment
- Python [3.15.2]; numpy, matplotlib, pytest, pennylane (see `requirements.txt`).

## Conventions
- Ranks are one-based: rank k is `sorted(x)[k-1]`.
- Unsigned integers, most significant bit first.
- Even N uses the lower median, k = ceiling(N/2).

## Result
[64/64 exhaustive tests pass.] The 3x3x3 counterexample is a fixed point
whose median (14, at (1,3,3)) is outside the central plane k=2. A candidate
set containing the target does not give the target's rank within that set.

