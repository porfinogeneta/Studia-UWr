import numpy as np
import math
import matplotlib.pyplot as plt

def binomial_coefficient(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def bernsteinPolynomial(n, i, t):
    return binomial_coefficient(n, i) * (t**(n-i)) * ((1-t)**i)

def bezier(control_points,weights, t):
    # numerator
    numerator = np.zeros_like(control_points[0])
    n = len(control_points) - 1

    # x_points, y_points = zip(*control_points)
    # curve_x = [0] * (len(control_points))
    # curve_y = [0] * (len(control_points))
    curve_x = 0
    curve_y = 0

    for i in range(len(control_points)):
        curve_x += bernsteinPolynomial(n,i, t) * control_points[i][0] * weights[i]
        curve_y += bernsteinPolynomial(n,i, t) * control_points[i][1] * weights[i]
    #
    # # denominator
    x = 0
    y = 0
    for i in range(len(weights)):
        x += bernsteinPolynomial(n, i, t) * weights[i]
        y += bernsteinPolynomial(n, i, t) * weights[i]

    curve_x = curve_x / x
    curve_y = curve_y / y

    # for x,y in zip(curve_x, curve_y):
    #     print(x, y)

    return curve_x, curve_y

def plot_curve(num_points,controls, weights):
    t = np.linspace(0, 1, num_points)
    curve_points = np.array([bezier(controls, weights, ti) for ti in t])

    plt.plot(curve_points[:, 0], curve_points[:, 1], label='Bezier Curve')
    plt.scatter(*zip(*controls), color='red', label='Control Points')
    plt.legend()
    plt.show()

# wagi służą przybliżaniu naszej 'bety' coraz bliżej do danego punktu,
# trochę na zasadzie magnesów
if __name__ == '__main__':
    # control points
    controls = [ (0.0, 0.0), (3.5, 36.0), (25.0, 25.0), (25.0, 1.5), (-5.0, 3.0), (-5.0, 33.0),
    (15.0, 11.0), (-0.5, 35.0), (19.5, 15.5), (7.0, 0.0), (1.5, 10.5)]
    weights = [1.0, 6.0, 4.0, 2.0, 3.0, 4.0, 2.0, 1.0, 5.0, 4.0, 1.0]
    plot_curve(1000, controls, weights)

