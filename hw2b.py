import math
import copy

def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    Use the Secant Method to find the root of fcn(x) in the neighborhood of x0 and x1.

    :param fcn: The function for which we want to find the root.
    :param x0: The first initial guess. (in neighborhood of root)
    :param x1: The second initial guess. (in neighborhood of root)
    :param maxiter: Maximum number of iterations. (exit if the number of iterations equals this number)
    :param xtol: Tolerance for convergence. (exit if xnewest - xprevious is less than xtol)
    :return: The final estimate of the root (most recent new x value).
    """

    # Initialize iteration counter and initial guesses
    iter_count = 0
    x_prev = copy.copy(x0)
    x_curr = copy.copy(x1)

    while iter_count < maxiter:
        # Calculate the new estimate using the Secant Method
        f_x_curr = fcn(x_curr)
        f_x_prev = fcn(x_prev)

        if f_x_curr == f_x_prev:
            raise ValueError("Secant method: Division by zero (function values are equal).")

        x_new = x_curr - f_x_curr * (x_curr - x_prev) / (f_x_curr - f_x_prev)

        # Check for convergence
        if abs(x_new - x_curr) < xtol:
            return x_new

        # Update values for the next iteration
        x_prev = copy.copy(x_curr)
        x_curr = copy.copy(x_new)

        iter_count += 1

    raise RuntimeError("Secant method did not converge within the specified number of iterations.")

def main():
    """
    Problem #1, Problem #2, Problem #3
    """
    fcn1 = lambda x: x - 3 * math.cos(x)
    x01 = 1
    x11 = 2
    maxiter1 = 5
    xtol1 = 1e-4

    root_estimate1 = Secant(fcn1, x01, x11, maxiter1, xtol1)
    print(f"Root estimate 1 : {root_estimate1:.5f}")

    fcn2 = lambda x: math.cos(2 * x) * x**3
    x02 = 1
    x12 = 2
    maxiter2 = 15
    xtol2 = 1e-8

    root_estimate2 = Secant(fcn2, x02, x12, maxiter2, xtol2)
    print(f"Root estimate 2 : {root_estimate2:.5f}")

    fcn3 = fcn2
    x03 = 1
    x13 = 2
    maxiter3 = 10
    xtol3 = 1e-8

    root_estimate3 = Secant(fcn3, x03, x13, maxiter3, xtol3)
    print(f"Root estimate 3 : {root_estimate3:.5f}")

if __name__ == "__main__":
    main()