from decimal import Decimal


# sumuje ceny netto, i bierze 23%
# type można użyć do zrobienia funkcji, które mogą przyjmować Decimal i float
def vat_faktura(lista):
    return sum(lista) * 0.23

def vat_faktura_deci(lista):
    return sum(lista) * Decimal('0.23')

def vat_paragon(lista):
    return sum(map(lambda x: x * 0.23, lista))

def vat_paragon_deci(lista):
    return sum(map(lambda x: x * Decimal('0.23'), lista))



if __name__ == '__main__':
    zakupy = [12.99, 2.98, 3.65, 9.12] #to nam nie działa
    zakupy2 = [12.0, 2.0, 3.0, 9.0]
    zakupy_deci = [Decimal('12.99'), Decimal('2.98'), Decimal('3.65'), Decimal('9.12')]

    # print(vat_faktura(zakupy2) == vat_paragon(zakupy2))
    # zamiana na Decimal sprawia, że ułamki zachowują się tak jak przęto w matematyce
    print(vat_faktura_deci(zakupy_deci) == vat_paragon_deci(zakupy_deci)) #case z użyciem Decimal
    print(vat_faktura(zakupy) == vat_paragon(zakupy)) #case dla floatów
    print(vat_faktura(zakupy2) == vat_paragon(zakupy2)) #case dla floatów całkowitych

