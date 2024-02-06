import copy

def is_diagonal_dominant(matrix):
    """
    Check and Modify the matrix to make it diagonally dominant if needed.
    """
    N = len(matrix)
    for i in range(N):
        diagonal_element = abs(matrix[i][i])
        row_sum = sum(abs(matrix[i][j]) for j in range(N) if j != i)

        if diagonal_element <= row_sum:
            scaling_factor = max(1, abs(diagonal_element) / (row_sum + 1e-9))
            matrix[i] = [element / scaling_factor for element in matrix[i]]

    return matrix


def GaussSeidel(Aaug, x, Niter=15):
    """
    Use the Gauss-Seidel method to estimate the solution to a set of linear equations Ax = b.
    :param Aaug: An augmented matrix containing [A|b] having N rows and N+1 columns, where N is the number of equations in the set.
    :param x: a vector (array) contains the values of the initial guess.
    :param Niter: the number of iterations (new x vectors) to compute.
    :return: the final new x vector.
    """
    Aaug = is_diagonal_dominant(copy.deepcopy(Aaug))  # Adjust matrix to make it diagonally dominant

    N = len(x)

    #check and modify matrix to diagonally dominant

    for k in range(Niter):
        x_prev = copy.deepcopy(x)
        for i in range(N):
            sigma = sum(Aaug[i][j] * x[j] for j in range(N) if j != i)
            x[i] = (Aaug[i][-1] - sigma) / Aaug[i][i]

    return x

def main():
    """
    Problem #1 and Problem #2 from HW2
    :return: two matrix with the answers to the augmented matrix provided.
    """
    Aaug1 = [[3, 1, -1, 2],
             [1, 4, 1, 12],
             [2, 1, 2, 10]]
    x1 = [0, 0, 0]
    Niter1 = 15
    solution1 = GaussSeidel(Aaug1, x1, Niter1)
    print("Solution 1:", [round(val, 3) for val in solution1])

    # Example 2
    Aaug2 = [[1, -10, 2, 4, 2],
             [3, 1, 4, 12, 12],
             [9, 2, 3, 4, 21],
             [-1, 2, 7, 3, 37]]
    x2 = [1, 1, 1, 1]
    Niter2 = 15
    solution2 = GaussSeidel(Aaug2, x2, Niter2)
    print("Solution 2:", [round(val, 3) for val in solution2])

if __name__ == "__main__":
    main()
