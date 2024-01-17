import matplotlib.pyplot as plt
import numpy as np

def getPoints():
    points = []
    with open ('punkty.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            x,y = line.split(',')
            points.append((float(x), float(y)))

    # sort points
    points.sort(key=lambda point: point[0])

    xs = []
    ys = []

    for pair in points:
        xs.append(pair[0])
        ys.append(pair[1])

    return xs,ys

# point (a)
def plotFunction(xs,ys):
    plt.plot(xs,ys, 'ro', markersize=2)

    def countRightFunction():
        formula = lambda t: (t - 1.2) * (t + 4.1) * (t - 2.3)
        values_y = [formula(t) for t in xs]
        plt.plot(xs, values_y, '-')

    # countRightFunction()

# point (b)
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


def create_formula(M,xs, ys):
    moments = [0] * (M+1)
    ts = xs
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

def splineInterpolation(xs,ys):

    M = 80

    formulas_y = create_formula(M,xs,ys)


    # drawing
    min_x = xs[0]
    max_x = xs[-1]
    interval = 0.1
    # we make a list of possible x's to apply
    args_x = np.arange(min_x, max_x, interval)
    args_x = np.clip(args_x, min_x, max_x).tolist()


    y_points = []
    # for every generated argument we find a suitable function
    # from the generated functions
    for a in args_x:
        for i, t in enumerate(xs):
            # compare it the point being added is in a specific spline range
            if a < t:
                y_points.append(formulas_y[i-1](a))
                break
    plt.plot(args_x, y_points, marker='o', linestyle='-', color='b',markersize=1)
    plt.show()


# point (c)
# xs are indexed from 0 to N, so there are N+1 x_i, have to pass N+1 here
# N length of xs + 1, n number of Polynomials
def generateOrthogonalPolynomials(N,n,xs):
    iterator = 1
    # list of values of two steps down polynomial
    P_prev_prev = [1] * N
    # list of values of one step down
    P_prev = [1] * N
    All_Polynomials = [P_prev]
    dot_product_P_prev_prev = sum([P_prev_prev[i] for i in range(N)])
    while iterator < n:

        # Ck part
        # denominator
        square_values_P_prev = [P_prev[i] * P_prev[i] for i in range(N)]
        dot_product_P_prev = sum(square_values_P_prev)
        # numerator
        dot_product_x_P_prev = sum([xs[i] * square_values_P_prev[i] for i in range(N)])
        c_k = dot_product_x_P_prev/dot_product_P_prev

        # count values of calculated polynomial for every 'x' and update values
        # dk part
        if iterator >= 2:
            d_k = dot_product_P_prev/dot_product_P_prev_prev
            # count every P for every xi
            P_new = [(xs[i] - c_k) * P_prev[i] - d_k * P_prev_prev[i] for i in range(N)]
        else:
            P_new = [(xs[i] - c_k) for i in range(N)]

        P_prev_prev = P_prev
        P_prev = P_new
        dot_product_P_prev_prev = dot_product_P_prev
        All_Polynomials.append(P_new)
        iterator += 1

    return All_Polynomials

# table with results of polynomials for each 'x',
# degree of created polynomial,
# values of function ad given point
# amount of x in 'xs' list
def approximate_function(degree, f, N, xs):

    # values of orthogonal polynomials from P0 to PN
    all_polynomials = generateOrthogonalPolynomials(N,degree+1,xs)
    print(all_polynomials)

    aas = []
    for d in range(degree + 1):
        dot_product_f_P_k = sum([f[i] * all_polynomials[d][i] for i in range(N)])
        dot_product_P_k = sum(all_polynomials[d][i]*all_polynomials[d][i] for i in range(N))
        aas.append(dot_product_f_P_k/dot_product_P_k)

    # approximated 'y' values for each 'x'
    results_y = [] # new 'y' values for given 'x' values
    for i in range(len(xs)):
        val_y = 0
        for d in range(degree+1):
            val_y += aas[d] * all_polynomials[d][i]
        results_y.append(val_y)

    return results_y





if __name__ == '__main__':
    points_x, points_y = getPoints()

    plotFunction(points_x,points_y)
    # plt.show()
    #
    # splineInterpolation(points_x,points_y)

    for d in range(2,16):
        # generateOrthogonalPolynomials(5,3, [-9,-6,0,6,9])
        res_y = approximate_function(d, points_y, 81, points_x)
        plt.plot(points_x, res_y, '-')

    plt.show()

