import numpy as np

A = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 14]],
    [[9, 10, 11], [12, 13, 15], [16, 17, 26]],
    [[18, 19, 20], [21, 22, 23], [24, 25, 27]],
]) 

def is_coordinate_increasing(grid):
    """
    true if the values in the grid are increasing along each coordinate axis
    """
    return all((np.diff(grid,axis=axis) >0).all() for axis in range(grid.ndim))

def median_position(grid):
    """
    returns lower median and its position in the grid
    """
    flat = sorted(grid.flatten())
    median = flat[len(flat + 1) // 2 - 1] #lower median
    pos = tuple(int(x) + 1 for x in np.argwhere(grid == median)[0]) # one based index
    return median, pos

if __name__ == "__main__":
    print("grid is coordinate increasing:", is_coordinate_increasing(A))
    median, pos = median_position(A)
    print(f"median: {median} at (i,j,k): {pos}")
    print("median 14 found in central plane k = 2:", pos[2] == 2)