import math

import numpy as np
import matplotlib.pyplot as plt




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt



    def generate_zeroes(n):
        h = 2.0/n
        res = [-1.0]
        for i in range(1, n+1):
            res.append(res[i-1] + h)
        return res

    def generate_chebyshev_nodes(n):
        k_values = np.arange(0, n + 1)
        zeroes = np.cos(((2 * k_values + 1) * math.pi) / ((2 * n) + 2))
        return zeroes

    print(generate_chebyshev_nodes(4))
    def evaluate_polynomial(zeroes, x):
        res = np.ones_like(x)
        for zero in zeroes:
            res *= (x - zero)
        return res

    # standard polynomial
    for n in range(50, 51):
        x_values = np.linspace(-1, 1, 1000)
        y_values = evaluate_polynomial(generate_zeroes(n), x_values)
        plt.plot(x_values, y_values, label=f'Order {n}')

    plt.title('Polynomial Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Chebyshev polynomial
    for n in range(50, 51):
        x_values = np.linspace(-1, 1, 1000)
        y_values = evaluate_polynomial(generate_chebyshev_nodes(n), x_values)
        plt.plot(x_values, y_values, label=f'Order {n}')

    plt.title('Chebyshev Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

