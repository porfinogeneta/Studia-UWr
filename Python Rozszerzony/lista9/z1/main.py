# TODO
# - pobranie danych i wyświetlenie ich na wykresach
# - dwa różne źródła, i dwa kolejne lata
# - dane z tego samego roku, ten sam wykres, X - miesiące, bardziej szczegółowe, uśrednić
# - wymyślić i zaprogramować na 3 wykresie prognozę
# TODO
# - wykresy na jednym obrazu
# - opisy
# - sekrety ewentualnie dodać
import json
from decimal import *
import matplotlib.pyplot as plt
import asyncio
import aiohttp

from aiohttp import ClientSession

async def fetch_data(session, url):
    async with session.get(url) as result:
        if result.status == 200:
            res = await result.text()
            return res
        else:
            print(f"Error: Request failed with status code {result.status}")
            return None

async def get_exchange_rates(years):
    # ten endpoint daje nam dane od roku 2023 do 2014, + kilka dni z każdego miesiąca

    urls = ["https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=USD&to_symbol=PLN&apikey=BC0MD1AENV7OXOVN"]
    # url_template = "http://api.nbp.pl/api/exchangerates/rates/a/usd/{year}-{month}-01/{year}-{month}-31/?format=json"
    # months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    # endpoints = [url_template.format(month=month, year=year) for year in range(years[0], years[1] + 1) for month in months]

    async with aiohttp.ClientSession() as session:
        requests = [fetch_data(session, url) for url in urls]
        # * odpakowuje nam listę, tworząc osobne argumenty dla funkcji
        return await asyncio.gather(*requests)

# USD -> PLN
def process_exchange_rates(json_data, exchange_res):
    # data = None
    # with open('z1/exchange_rates.json', 'r') as file:
    #     data = json.load(file)
    data = json.loads(json_data)
    print(data)
    # wyciągamy z JSONa kolejne miesiące
    time_series = data["Time Series FX (Monthly)"]

    for date, values in time_series.items():
        # pobieramy rok, przerabiamy go na liczę
        year = int(date.split('-')[0])
        # jak ten rok nas interesuje, pobieramy miesiąc i uśredniamy 'high' i 'low'
        if year in years:
            # pobieramy miesiąc, który powie nam na który indeks dodać
            month_str = date.split('-')[1]
            # jak nasz miesiąc się zacznie od zera musimy przerobić go na normalną liczbę
            if month_str[0] == '0':
                month_str = month_str[1]
            month = int(month_str) # również przerabiamy na liczbę
            # używamy Decimal, bo pieniędzy nie liczy się na floatach
            high = Decimal(values['2. high'])
            low = Decimal(values['3. low'])
            exchange_res[year].append(float( Decimal((high + low)) / Decimal(2))) # uśredniam górną i dolną cenę



async def get_inflation_data(years):
    # okres [247,258] -> styczeń grudzień
    url = "https://api-dbw.stat.gov.pl/api/1.1.0/variable/variable-data-section?id-zmienna=305&id-przekroj=736&id-rok={year}&id-okres={month}&ile-na-stronie=5000&numer-strony=0&lang=pl?&id-sposob-prezentacji-miara=5"
    endpoints = [url.format(month = i, year = j) for i in range(247,259) for j in range(years[0], years[1] + 1)]

    async with aiohttp.ClientSession() as session:
        requests = [fetch_data(session, url) for url in endpoints]
        # * odpakowuje nam listę, tworząc osobne argumenty dla funkcji
        return await asyncio.gather(*requests)



def process_inflation(json_data, inflation_res):
    data = json.loads(json_data)
    data_array = data["data"]
    # 2 element to jest zawsze analogiczny miesiąc poprzedniego roku
    # mamy 'id-sposob-prezentacji-miara' = 5, 'analogiczny okres roku poprzedniego'
    inflation_obj = next((obj for obj in data_array if obj['id-sposob-prezentacji-miara'] == 5), None)
    inflation = inflation_obj["wartosc"]

    # dla ujednolicenia danych tutaj też checmy otrzymać słownik
    inflation_res[int(inflation_obj['id-daty'])].append(inflation)

# funkcja do obliczania ilorazu różnicowego, zrobię interpolację Newtona
# i po prostu 'przedłużymy' sobie ten wykres
def differential_quotient(x_values, y_values, res, order):
    # na początku dodajemy pierwszą wartość, jako pierwszy iloraz różnicowy
    res.append(y_values[0])
    # ilorazów różnicowych będzie tyle ile mamy x-ów
    if order == len(x_values):
        return res
    help = []
    for i in range(len(y_values) - 1):
        help.append((y_values[i+1] - y_values[i])/(x_values[i+order] - x_values[i]))
    return differential_quotient(x_values, help, res, order + 1)

def plot_data(inflation_res, exchange_res, years):
    # inflacja jest z bazą 100, czyli waktyczny procent uzyskamy po odjęciu 100
    inflation_res_100_based = {year: [round(value - 100, 2) for value in values] for year, values in
                               inflation_res.items()}

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    plt.figure(figsize=(14, 6))

    for year in years:
        plt.plot(months, inflation_res_100_based[year], label=f'Inflation {year} to same month last year', marker='o')
        plt.plot(months, exchange_res[year], label=f'Exchange {year}', marker='o')



        plt.title(f"Inflation and USD Exchange Rate in {year}")
    plt.xlabel("Months")
    plt.ylabel("Exchange Rate (USD->PLN) and Inflation (100 based)")
    plt.legend()
    plt.show()


# funkcja do obliczania wartości danego x
import math
import numpy as np
def apply_x(x_poly, x_nodes, differential_quotient):
    # jakiś problem natury numerycznej
    # res = differential_quotient[0]
    # for i in range(1, len(x_nodes)):
    #     help = math.prod([(x_poly - x_nodes[j - 1]) for j in range(1, i+1)])
    #     res += differential_quotient[i] * help
    # return res
    order = 1
    res = differential_quotient[0]
    while order < len(x_nodes) - 1:
        help = 1
        # iloczyn argumentów (x - x0)*...*(x - x_n-1)
        # ten for to blok an*(x - x0)*...*(x - x_n-1), gdzie a_i to iloraz różnicowy
        for i in range(1, len(x_nodes) - order):
            help *= (x_poly - x_nodes[i-1])
            # w ostatniej iteracji przemnażamy przez iloraz różnicowy
            if i == len(x_nodes) - order - 1:
                help *= differential_quotient[i]

        res += help
        order += 1
    return res

# funkcja dla nowego danych argumentów i danych ilorazów różnicowych policzy wartość wielomianu
# x_polynomial to argumenty wielomianu, x_i to węzły wielomianu
def count_polynomial(x_polynomial, x_nodes, differential_quotient):
    # lista na przewidziane wartości wielomianu
    return [round(apply_x(x, x_nodes, differential_quotient), 2) for x in x_polynomial]

def predict(years, inflation_res, exchange_res):
    # weźmy wartości x do naszego wielomianu
    # argumentami interpolowanego wielomianu będzie ułamek 1/(liczba miesięczy okresu badanaego)
    x_values = [round(i / (12 * len(years)), 2) for i in range(1, 12 * len(years) + 1)]

    # inflation
    y_values_inflation_gather = [inflation_res[year] for year in years]
    y_values_inflation = []
    for elem in y_values_inflation_gather:
        y_values_inflation += elem

    # exchange rates
    y_values_exchange_gather = [exchange_res[year] for year in years]
    y_values_exchange = []
    for elem in y_values_exchange_gather:
        y_values_exchange += elem

    # teraz wygenerujemy wielomian interpolacyjny dla inflacji i wymiany
    # liczymy ilorazy różnicowe
    differential_quotient_inflation = differential_quotient(x_values, y_values_inflation, [], 1)
    differential_quotient_exchange = differential_quotient(x_values, y_values_exchange, [], 1)


    # tworzymy wielomian interpolacyjny
    # argumentami będą ułamki - od (25 miesiąc/ wszystkie miesiące) do 1
    x_new_args = [round(i / (12 * (len(years) + 1)), 2) for i in range(12 * len(years), 12 * (len(years) + 1))]

    # print(count_polynomial(x_new_args, x_values, differential_quotient_inflation))
    # print(count_polynomial(x_new_args, x_values, differential_quotient_exchange))
    y_inflation_prediction = count_polynomial(x_new_args, x_values, differential_quotient_inflation)
    y_exchange_prediction = count_polynomial(x_new_args, x_values, differential_quotient_exchange)

    print(y_inflation_prediction)
    print(y_exchange_prediction)

    # dodajemy predykcje do słownika
    next_year = max(years) + 1
    inflation_res[next_year] = y_inflation_prediction
    exchange_res[next_year] = y_exchange_prediction
    # dodajemy do lat nowy, przewidziany rok
    years.append(next_year)


# inflacja względem analogicznego miesiąca poprzedniego roku
# dodaję teź plik JSON bo API czasem nie współpracuje
if __name__ == '__main__':
    years = [2021, 2022]
    # POBRANIE DANYCH Z API
    inflation_res = {}
    exchange_res = {}
    # tworzymy słownik, klucz to konkretny rok, a wartość to kursy wymiany z konkretnych miesięcy [...] lista
    for i in range(len(years)):
        inflation_res[years[i]] = []
        exchange_res[years[i]] = []

    for elem in asyncio.run(get_inflation_data(years)):
        process_inflation(elem, inflation_res)

    for elem in asyncio.run(get_exchange_rates(years)):
        process_exchange_rates(elem, exchange_res)


    # NARYSOWANIE DANYCH
    # inflation_res = {2021: [102.5, 102.4, 103.2, 104.5, 104.9, 104.5, 105.1, 105.5, 105.9, 106.9, 107.8, 108.6],
    #  2022: [109.3, 108.4, 110.9, 112.2, 113.8, 115.4, 115.4, 115.8, 116.8, 117.5, 117.1, 116.3]}
    # exchange_res = {2021: [4.0739, 4.071415, 3.961155, 3.90026, 3.872195, 3.847, 3.74185, 3.73591, 3.8555, 3.855575, 3.7227, 3.712105],
    #  2022: [4.43185, 4.65048, 4.8676, 4.830815, 4.66418, 4.6648, 4.395925, 4.380525, 4.33745, 4.382665, 4.07572,
    #         4.0321]}

    # narysowanie wykresu bez przewidywań
    plot_data(inflation_res, exchange_res, years)

    # PRZEWIDYWANIE PRZYSZŁOŚCI
    predict(years, inflation_res, exchange_res)

    # print(inflation_res)
    # print(exchange_res)

    plot_data(inflation_res, exchange_res, years)


    # print(differential_quotient([-4,-3,-2,2,3,4], [9,7,5,-3,-5,1977], [], 1))