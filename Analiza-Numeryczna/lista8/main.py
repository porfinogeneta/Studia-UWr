import matplotlib.pyplot as plt
import numpy as np
def difference_quotient(args, values, order):
    if order == 3:
        return values
    else:
        res = []
        for i in range(len(values) - 1):
            res.append((values[i+1] - values[i])/(args[i+order] - args[i]))
        return difference_quotient(args, res, order + 1)

def Q_and_U(ts, ys, M):
    ds = [6 * i for i in difference_quotient(ts, ys, 1)]
    # [0, q1, ..., q_n-1]
    Q = [0] * M
    U = [0] * M

    for i in range(1, M):
        lambda_i = (ts[i] - ts[i-1])/(ts[i+1] - ts[i-1])
        p = lambda_i * Q[i-1] + 2
        Q[i] = (lambda_i - 1) / p
        U[i] = (ds[i-1] - lambda_i*U[i-1]) / p

    return Q,U

def count_moment(Q, U, k, moments):
    if k == 0:
        return
    else:
        moments[k] = U[k] + Q[k] * moments[k+1]
        count_moment(Q, U, k-1, moments)


def create_formula(M, ys):
    moments = [0] * (M+1)
    ts = [i/M for i in range(M+1)]
    Q,U = Q_and_U(ts, ys, M)
    count_moment(Q,U,M-1,moments)
    S = []

    for k in range(1, M + 1):
        hk = ts[k] - ts[k - 1]
        S.append(lambda t, k=k, moments=moments, ts=ts, ys=ys, hk=hk: (1 / hk) * (
                ((1 / 6) * moments[k - 1] * (ts[k] - t) ** 3) + (1 / 6) * moments[k] * ((t - ts[k - 1]) ** 3) +
                (ys[k - 1] - (1 / 6) * moments[k - 1] * (hk ** 2)) * (ts[k] - t) + (
                            ys[k] - (1 / 6) * moments[k] * hk ** 2) * (t - ts[k - 1])
        ))

    return S



if __name__ == '__main__':
    M = 95
    # # nodes are starting from 0
    # nodes = [i/M for i in range(M+1)]
    values_x = [5.5, 8.5, 10.5, 13, 17, 20.5, 24.5, 28, 32.5, 37.5, 40.5, 42.5, 45, 47,
49.5, 50.5, 51, 51.5, 52.5, 53, 52.8, 52, 51.5, 53, 54, 55, 56, 55.5, 54.5, 54, 55, 57, 58.5,
59, 61.5, 62.5, 63.5, 63, 61.5, 59, 55, 53.5, 52.5, 50.5, 49.5, 50, 51, 50.5, 49, 47.5, 46,
45.5, 45.5, 45.5, 46, 47.5, 47.5, 46, 43, 41, 41.5, 41.5, 41, 39.5, 37.5, 34.5, 31.5, 28, 24,
21, 18.5, 17.5, 16.5, 15, 13, 10, 8, 6, 6, 6, 5.5, 3.5, 1, 0, 0, 0.5, 1.5, 3.5, 5, 5, 4.5, 4.5, 5.5,
6.5, 6.5, 5.5]
    values_y = [41, 40.5, 40, 40.5, 41.5, 41.5, 42, 42.5, 43.5, 45, 47, 49.5, 53, 57, 59,
59.5, 61.5, 63, 64, 64.5, 63, 61.5, 60.5, 61, 62, 63, 62.5, 61.5, 60.5, 60, 59.5, 59, 58.5,
57.5, 55.5, 54, 53, 51.5, 50, 50, 50.5, 51, 50.5, 47.5, 44, 40.5, 36, 30.5, 28, 25.5, 21.5,
18, 14.5, 10.5, 7.50, 4, 2.50, 1.50, 2, 3.50, 7, 12.5, 17.5, 22.5, 25, 25, 25, 25.5, 26.5,
27.5, 27.5, 26.5, 23.5, 21, 19, 17, 14.5, 11.5, 8, 4, 1, 0, 0.5, 3, 6.50, 10, 13, 16.5, 20.5,
25.5, 29, 33, 35, 36.5, 39, 41]

    formulas_x = create_formula(M, values_x)
    formulas_y = create_formula(M, values_y)

    ts = [i / M for i in range(M + 1)]


    # drawing
    drawing_M = 500
    draw_args = [i/drawing_M for i in range(drawing_M + 1)]

    x_points = []
    y_points = []
    # for every generated argument we find a suitable function
    # from the generated functions
    for a in draw_args:
        for i, t in enumerate(ts):
            if a < t:
                x_points.append(formulas_x[i-1](a))
                y_points.append(formulas_y[i-1](a))
                break

    # adding first point at the end of an array to connect all points with polyline
    x_points.append(x_points[0])
    y_points.append(y_points[0])
    plt.plot(x_points, y_points, marker='o', linestyle='-', color='b',markersize=1)
    plt.show()
