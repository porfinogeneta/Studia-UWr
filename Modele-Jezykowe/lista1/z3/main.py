from review_determine import ReviewDetermine

if __name__ == "__main__":

    opinions = ["Drożej niż u konkurencji w podobnym standardzie.", "Kiepskie warunki, słaba obsługa",
             "Omijaj to miejsce!", "Generalnie mogę go polecić, kierował mnie na potrzebne badani",
             "Serdeczne pozdrowienia dla Pani Dr Dominiki Tuchendler oraz Dr Szymczaka, który zaraża swoim spokojem i opanowaniem pacjentów.",
             "Nie polecam innych pokoi - widoki niekoniecznie ucieszą...", "Polecam ten hotel - świetny widok, super dojazd.", "Super genialne miejsce, coś wspaniałego!!!"]

    reviewer = ReviewDetermine()
    reviewer.calculate_accuracy(filename="reviews.txt", pos_neg=[" - polecam", " - nie polecam"], every_ith=1)
    # reviewer.check_opinions(opinions, [" - ocena: pozytywna.", " - ocena: negatywna."])
    # reviewer.calculate_accuracy("reviews.txt", [" - ocena: pozytywna.", " - ocena: negatywna."])
    # reviewer.calculate_accuracy("reviews.txt", [" - ocena: pozytywna.", " - ocena: negatywna."], 4)
    # reviewer.calculate_accuracy("reviews.txt", ["- pozytywna", "- negatywna"], every_ith=4)















    # # większa liczba znaczy lepiej
    # pos_neg_1 = [
    # ' opinia: pozytywna',
    # ' opinia: negatywna',
    # ]


    # # dostajemy wyniki w skali logarytmicznej
    # res1 = [SentenceProabability.sentence_prob(s) for s in pos_neg_1]

    # log_prob_pos = res1[0]
    # log_prob_neg = res1[1]

    # # zamieniamy na skalę liniową
    # lin_prob_pos = math.exp(log_prob_pos)
    # lin_prob_neg = math.exp(log_prob_neg)
    # # print(lin_prob_pos)
    # # print(lin_prob_neg)

    # # normalizujemy prawdopodobieństwa, jedmy prawdopodobieństwem jest pos drugim neg
    # total = lin_prob_pos + lin_prob_neg
    # pos = lin_prob_pos / total
    # neg = lin_prob_neg / total
    # scale = pos / neg
    # print("positive probability: ", pos)
    # print("negative probability: ", neg)
    # print("after scaling neg:", neg * scale)


    # for s in sentences:
    #     print(s)
    #     print(determine_opinion(s, pos_neg_1[0], pos_neg_1[1], scale))
    # # print ()
    # # for s in sentences1:
    # #     prob = SentenceProabability.sentence_prob(s)
    # #     print(type( prob))
    # #     print (s, prob)