
def compress(text):
    # dwie wersje, bo dla wyrazu aabbccaabbcc mamy zwrócić:
    # [('a': 4, 'b':4, 'c':4)] (1 wersja), czy [('a': 2, 'b':2, 'c':2, 'a': 2, 'b':2, 'c':2)] (2 wersja)
    # create a list of list of tuples with compressed words
    # return [list({letter: w.count(letter) for letter in w}.items()) for w in text.split(" ")]
    # generate a list of list of tuples
    words = text.split(" ")
    compr = []
    for w in words:
        compr_w = []
        acc = w[0]
        lc, i = 0,0
        while i <= len(w):
            if not i == len(w) and w[i] == acc:
                lc += 1
            else:
                compr_w.append([acc, lc])
                if not i == len(w):
                    acc = w[i]
                    lc = 1
            i += 1
        compr.append(compr_w)
    return [[tuple(lst) for lst in cmpr_w] for cmpr_w in compr]



def decompress(compr):
    # decm = ""
    # "".join(("".join(key*value for key, value in cw) + " ") for cw in compr)
    # for cw in compr:
    #     decm += ("".join(key*value for key, value in cw) + " ")
    # we build string from decoded words in cw, from compr
    return "".join(("".join(key*value for key, value in cw) + " ") for cw in compr)




if __name__ == '__main__':
    print(compress('suuuuper maxim'))
    print(compress('maxim'))
    print(decompress(compress('suuuuper maxim')))

    file = "lalka.txt"
    with open(file, 'r') as file:
        contents = file.read()

    print(decompress(compress(contents)))
