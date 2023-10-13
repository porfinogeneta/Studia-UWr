import random



def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
    krotkie = [slowo for slowo in tekst.split(" ") if dl_slowa >= len(slowo) > 0]
    while len(krotkie) > liczba_slow:
        del krotkie[random.randint(0, len(krotkie) - 1)]
    # punctuation mark at the end
    if krotkie and (krotkie[-1][-1]).isalpha():
        krotkie[-1] += '.'
    #sentence begins with a big letter
    if krotkie and (krotkie[0][0]).islower():
        krotkie[0] = krotkie[0][0].upper() + krotkie[0][1:]
    return " ".join(krotkie)


if __name__ == '__main__':
    tekst = "Podział peryklinalny inicjałów wrzecionowatych \
    kambium charakteryzuje się ścianą podziałową inicjowaną \
    w płaszczyźnie maksymalnej!"

    file = "lalka.txt"
    with open(file, 'r') as file:
        contents = file.read()

    zdania = contents.split(". ")
    uproszczone = map(lambda zd: uprosc_zdanie(zd, 15, 7), zdania)
    print(" ".join(uproszczone))