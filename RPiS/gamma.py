import math

def gamma(num):
    if num == 0.5:
        return math.sqrt(math.pi)
    elif num == 1:
        return 1
    else:
        return (num - 1) * gamma(num - 1)