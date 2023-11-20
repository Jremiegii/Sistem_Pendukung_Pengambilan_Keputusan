import numpy as np
from scipy.optimize import linear_sum_assignment

def hungarian_method(cost_matrix):
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return list(zip(row_ind, col_ind))

def transport_problem_hungarian(grid):
    cost_matrix = np.array(grid)
    result_indices = hungarian_method(cost_matrix)

    total_cost = 0
    solution_matrix = np.zeros_like(cost_matrix)

    for row, col in result_indices:
        allocation = cost_matrix[row][col]
        total_cost += allocation
        solution_matrix[row][col] = allocation

    return total_cost, solution_matrix

# Data
# grid = [[14, 5, 7, 8], [2, 12, 6, 5], [7, 8, 3, 9], [2, 4, 6, 10]]
# grid = [[15, 10, 9], [9, 15, 10], [10, 12, 8]]
grid = [[1, 4, 6, 3], [9, 7, 10, 9], [4, 5, 11, 7], [8, 7, 8, 5]]

# Solusi menggunakan Hungarian Method
result, solution_matrix = transport_problem_hungarian(grid)

# Output
print("Total biaya dengan metode Hungarian:", result)
print("Matriks solusi dengan metode Hungarian:")
print(solution_matrix)