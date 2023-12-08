# This is a sample Python script.

# order + 1 is amount of 'args' in difference quotient for example order( f[x0,x1]) + 1 = 2
def difference_quotient(args, values, order):
    if order == 3:
        return values
    else:
        res = []
        for i in range(len(values) - 1):
            res.append((values[i+1] - values[i])/(args[i+order] - args[i]))
        return difference_quotient(args, res, order + 1)

# counting q and u from a lecture algorithm
# N - amount of nodes, ts nodes
def Q_and_U(M, ts, values):
    d = [6*elem for elem in difference_quotient(ts, values, 1)]
    print(d)
    Q = [0] * M
    U = [0] * M
    for i in range(1, M):
        lambda_i = (ts[i] - ts[i-1])/(ts[i+1] - ts[i-1])
        p = lambda_i * Q[i-1] + 2
        Q[i] = (lambda_i - 1) / p
        # d[i-1] is i f[x_i-1, xi, x_i+1]
        U[i] = (d[i-1] - lambda_i * U[i-1]) / p

    return Q,U

# k is the moment to count
# M0=MN = 0, M is array of Moments, U and Q are the arrays of variables from algorithm, N number of nodes
# def count_moment(Q, U, k, N, M):
#     if k == N -1 :
#         M[k] = U[k]
#     else:
#         M[k] = U[k] + Q[k] * count_moment(U, Q, k+1, N, M)
#
def count_moment(M, k, moments, Q, U):
    if k == M or k == 0:
        moments[k] = 0
    else:
        moments[k] = U[k] + Q[k] * moments[k+1]
    if k != 0:
        count_moment(M, k - 1, moments, Q, U)
    else:
        return

# M - M for the exercise, ts are nodes, N - N from exercise, values - function values in nodes
def evaluate_formula(M, values):
    moments = [0] * (M+1)
    ts = [t / M for t in range(M+1)]
    Q, U = Q_and_U(M, ts, values)
    # print(Q, len(Q))
    # print(U, len(U))
    count_moment(M, M, moments, Q, U)
    print(moments)
    # list of splines
    S = []
    for k in range(1, M):
        hk = ts[k] - ts[k-1]
        S.append(lambda t: (1.0/hk) * (( 1.0/6.0 * moments[k-1] * (ts[k] - t)**3) + ( 1.0/6.0 * moments[k] * (t - ts[k-1])**3) +
                                    (values[k-1] - (1.0/6.0 * moments[k-1] * hk**2))*(ts[k] - t) +
                                    (values[k] - (1.0/6.0 * moments[k] * hk**2))*(t - ts[k-1]) ) )
    return S

#    # [-27075.0, 13537.499999999989, 40612.50000000003, -13537.500000000004, 13537.499999999935, -13537.499999999873, 27074.999999999858, 13537.499999999995, -54149.99999999988, -27075.000000000095, 13537.499999999985, -13537.499999999985, 13537.500000000182, -40612.5000000002, -13537.499999999985, 0.0, 13537.499999999985, -13537.499999999985, -18952.5000000001, -16244.999999999836, 8122.499999999913, 54149.99999999994, -13537.499999999989, 6.885159109515376e-11, -1.4175327578413994e-10, -40612.49999999993, -13537.500000000058, 13537.500000000093, 40612.49999999999, 27074.99999999976, -13537.499999999734, -27075.000000000116, 54150.00000000016, -40612.500000000175, -1.4175327578413994e-10, -40612.49999999993, -27074.999999999833, -27075.000000000262, -40612.50000000017, 67687.50000000032, 13537.499999999807, -27074.99999999976, 27074.99999999976, 40612.50000000017, 13537.49999999988, -40612.49999999993, -27074.999999999833, 0.0, -4.2930992094625346e-10, 27075.0000000004, 13537.499999999916, 0.0, 13537.499999999985, 27074.999999999825, -40612.499999999956, -40612.499999999956, -40612.499999999745, 27074.999999999825, 67687.50000000007, -13537.500000000131, -13537.499999999916, -27075.0000000004, -13537.49999999956, -27074.999999999825, 0.0, -13537.500000001, -13537.499999998978, 27074.999999999836, 13537.499999999269, 40612.50000000067, 0.0, -13537.500000000415, -13537.49999999956, -27074.999999999825, 27074.999999999825, -5.751132903242263e-10, 54150.000000000524, 0.0, -13537.500000000131, -40612.49999999981, -13537.499999999918, 40612.499999999745, 27074.99999999997, 13537.499999999985, 13537.499999999916, 27075.000000000553, -13537.500000000564, -40612.499999999745, -13537.500000000131, 13537.500000000131, 27074.999999999833, 0.0, -27074.99999999997, -27074.99999999997]
if __name__ == '__main__':
    # print([elem*6 for elem in difference_quotient([-4, -3, -2,2,3,4], [9,7,5,-3,-5,1977], 1)])
    # M jest o 1 mniej niż nodów, bo nodów jest M+1
    M = 95
    formulas = evaluate_formula(M, [5.5, 8.5, 10.5, 13, 17, 20.5, 24.5, 28, 32.5, 37.5, 40.5, 42.5, 45, 47,
49.5, 50.5, 51, 51.5, 52.5, 53, 52.8, 52, 51.5, 53, 54, 55, 56, 55.5, 54.5, 54, 55, 57, 58.5,
59, 61.5, 62.5, 63.5, 63, 61.5, 59, 55, 53.5, 52.5, 50.5, 49.5, 50, 51, 50.5, 49, 47.5, 46,
45.5, 45.5, 45.5, 46, 47.5, 47.5, 46, 43, 41, 41.5, 41.5, 41, 39.5, 37.5, 34.5, 31.5, 28, 24,
21, 18.5, 17.5, 16.5, 15, 13, 10, 8, 6, 6, 6, 5.5, 3.5, 1, 0, 0, 0.5, 1.5, 3.5, 5, 5, 4.5, 4.5, 5.5,
6.5, 6.5, 5.5])

    nodes = [t/M for t in range(M+1)]

    for i in range(1, len(nodes)):
        print(formulas[i-1](nodes[i]))
    # print(nodes)
    # print(len(formulas))
    # evaluated = [0] * len(nodes)
    # 01 12 23 34 ...
    # print(formulas[0](nodes[0]))
    # for i in range(len(formulas)):
    #     print(f"{i} {formulas[i](nodes[i])}")
    #     print(f"{i+1} {formulas[i](nodes[i+1])}")
    #     print("")
