#a of HW 2 (probability)
import math
import copy

def PDF (x, mu, sigma):
    """
    Gaussian/normal probability density function.

    """
    pdf = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    return pdf

def simpsons_rule(func, a, b, n, args):
    """
    Numerical integration using the trapezoidal rule.

    """
    h = (b - a) / n
    result = func(a, *args) + func(b, *args)

    for i in range (1, n, 2):
        result += 4 * func(a + i * h, *args)

    for i in range (2, n-1, 2):
        result += 2 * func(a + i * h, *args)

    return result * h / 3.0

def Probability(PDF, args, c, GT=True):
    """
    Calculate the probability of x being greater than or less than a given value.
    :param PDF: A callback function for the Gaussian/normal probability density function.
    :param args: A tuple containing the values for mu and sigma.
    :param c: A floating point value containing the upper limit of integration.
    :param GT: A boolean indicating if we want the probability of x being greater than c (True) or less than c (False).
    :return: The calculated probability (float).
    """
    mu, sigma = args # syntax used to unpack the values of args tuple into variables mu and sigma

    n = 1000 #number of intervals for the trapezoidal rule

    if GT:
        # when probability of x being greater than c
        result = simpsons_rule(PDF, c, mu + 5 * sigma, n, args)
    else:
        # when probability of x being less than c
        result = simpsons_rule(PDF, mu - 5 * sigma, c, n, args)
    return result

def main():
    """

    Problem 1 : x<105 with mean = 100 and standard deviation = 12.5

    Problem 2 : x> (mean)+2*(standarad deviation) with mean = 100 and standard deviation = 3


    """
    args_values = (100, 12.5) #mu is 100 and sigma is 12.5
    c_value = 105 #upper limit of 105 for this example of normal distribution
    probability = Probability(PDF, args_values, c_value, GT=False) #GT = False because you want the probability of x being less than c = 105.

    print(f"P(x < {c_value:.2f} | N({args_values[0]}, {args_values[1]})) = {probability:.2f}")

    args_values2 = (100, 3) #mu is 100 and sigma is 3
    c_value2 = args_values2[0] + 2 * args_values2[1]
    probability2 = Probability(PDF, args_values2, c_value2, GT=True) #GT = True becaues you want the probability of x being greater than c_value2

    print(f"P(x < {c_value2:.2f} | N({args_values2[0]} , {args_values2[1]})) = {probability2:2f}")

if __name__ == "__main__":
    main()