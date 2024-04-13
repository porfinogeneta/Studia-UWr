import math


def countMinDistances(pnts, n):
    minVal = float("inf")
    for i in range(n):
        for j in range(i+1, n):
            minVal = min(dist(pnts[i], pnts[j]), minVal)

    return minVal

def dist(a, b):
    return math.sqrt((a[0] - b[0])*(a[0] - b[0]) + (a[1] - b[1])*(a[1] - b[1]))


def calculateStripDist(d, pnts, size):
    minVal = d
    for i in range(size):
        for j in range(i+1, size):
            minVal = min(dist(pnts[i], pnts[j]), minVal)

    return minVal

def calculateShortes(points, n):

    # dla małej liczby punktów obliczamy ze wzoru
    if n <= 3:
        return countMinDistances(points, n)
    
    mid = len(points)//2
    # obliczamy najkrótszy dystans dla lewej i prawej części
    dl = calculateShortes(points, mid)
    dr = calculateShortes(points[mid:], n - mid)

    # obliczamy szerokość dostępnego pasa dla punktów
    d = min(dl, dr)
    # obliczamy równanie prostej, czyli średnią arytmetyczną odległości między dwoma punktami w połowie tablicy
    x = (points[len(points)//2 - 1][0] + points[len(points)//2][0]) / 2

    # pozbywamy się punktów dalszych niz d od prostej
    strip = []
    for i in range(n):
        if abs(points[i][0] - x) < d:
            strip.append(points[i])

    strip.sort(key=lambda point: point[1])

    dStrip = calculateStripDist(d, strip, len(strip))

    return min(d, dStrip)


def allTraingles(points, n):
    triangles = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                triangles.append(([points[i], points[j], points[k]]))

    return triangles

if __name__ == "__main__":
    # points = [(0, 0), (0, 1), (1, 0), (1, 1)]
    # points = [(2, 3), (12, 30), (40, 50), (5, 1), (12,10), (3,4)]
    # sortujemy względem x
    # points.sort(key=lambda point: point[0])
    
    # print(calculateShortes(points, len(points)))

    print(len(allTraingles("abcde", 5)))