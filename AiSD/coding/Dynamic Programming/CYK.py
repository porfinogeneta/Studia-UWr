

def cyk(word):
    # kolejne rzędy
    for l in range(1, len(word) + 1):
        # kolejne podsłowa
        for s in range(len(word) - l + 1):
            print("\n=================\n" + word[s:s+l], end='\n=================\n')
            # kolejne podziały podsłów
            for p in range(1, l):
                print(word[s:p+1], end=' ')
                print(word[p:p+l-1])
        print("")



if __name__ == "__main__":
    cyk("baaba")