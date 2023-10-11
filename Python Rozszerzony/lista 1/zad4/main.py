import math
import random


# rzuty, możliwy błąd, bok kwadratu i 2x promień okręgu
def pi_esti(thrw_c, epsilon, size):
    try:
        # sprawdzenie czy rzuty to liczba całkowita
        if isinstance(thrw_c, int):
            cltwt = 0  # wszystkie rzuty
            ltwo = 0  # trafienia w tarczę
            for t in range(thrw_c):
                # losowy punkt, nasz rzut  (kwadrat ma środek w układzie współrzędnych)
                point = (random.uniform(-(size / 2), size / 2), random.uniform(-(size / 2), size / 2))
                # czy, jesteśmy w kole, liczymy dzługość odcinka od (0,0)
                dist = math.sqrt(point[0] ** 2 + point[1] ** 2)
                if dist <= size / 2:
                    ltwo += 1  # trafiony
                cltwt += 1
                estimation = (4 * ltwo) / cltwt
                print(f"Pi estimation: {estimation}")
                if abs(estimation - math.pi) < epsilon:
                    print("End, accuracy accomplished!")
                    break
                if t == thrw_c - 1:
                    print("End count due to lack of shots")


    except:
        print("Throw Count has to be an integer!")


if __name__ == '__main__':
    pi_esti(1200, 0.01, 20)
