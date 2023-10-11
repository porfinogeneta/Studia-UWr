# używać generatorów
def is_palindrome(text):
    # reformat string
    # isalpha sprawdza czy jest to litera
    reipt = ""
    for sign in text.lower():
        # nie jest znakiem białym ani znakiem przestanokowym
        if not sign.isspace() and sign not in ",.!:;":
            reipt += sign
    return reipt[::] == reipt[::-1]

if __name__ == '__main__':
    print(is_palindrome("Míčo močím"))
    print(is_palindrome("Eine güldne, gute Tugend: Lüge nie!"))


