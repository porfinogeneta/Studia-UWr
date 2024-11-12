import random
from typing import Tuple
# FEW SHOTS LEARNING

# DODAWANIE
ADDITION = {
    "addition_one_digit": """
        <s><<SYS>>Jesteś prostym kalkulatorem, który jest w stanie dodawać dwie liczby do siebie. Dla danego wyrażenia obliczasz jego sumę.<</SYS>>
        [INST] Policz mi podane wyrażenie: 2 + 2[/INST]
        4
        [INST] Policz mi podane wyrażenie: 1 + 5[/INST]
        6
        [INST] Policz mi podane wyrażenie: 7 + 8[/INST]
        15
        [INST] Policz mi podane wyrażenie: 0 + 8[/INST]
        8
        [INST] Policz mi podane wyrażenie: {n1} + {n2}[/INST]
        """,

    "addition_rigid": """3 + 6 = 9
        2 + 1 = 3
        0 + 5 = 5
        7 + 0 = 7
        9 + 7 = 16
        {n1} + {n2} = """,

    "addition_one_digit_cot": """
    <s><<SYS>>Jesteś uczniem. Dzisiaj postanowiłeś nauczyć się dodawać do siebie dwie liczby jednocyfrowe. Rozwiążesz
    to zadanie krok po kroku.<</SYS>>
    
    1. Rozpoznaj liczby: Najpierw spójrz na dwie liczby, które mamy dodać.
        Jakie to liczby? (Na przykład, jeśli zadanie to 3 + 5, nasze liczby to 3 i 5.)

    2. Policz w górę: Zacznij od pierwszej liczby i dodawaj do niej kolejne liczby.
        Jeśli mamy 3, dodajemy 5. Jakie liczby wypowiadamy, licząc w górę? (Pomyśl: 4, 5, 6, 7, 8.)

    [INST]Znajdź odpowiedź: Ostatnia liczba, którą wypowiedziałeś, to wynik! Jaki więc jest wynik {n1} + {n2}?[/INST]
    """,
}

SUBSTRACTION = {
    "substraction_one_digit": """
        <s><<SYS>>Jesteś prostym kalkulatorem, który jest w stanie odejmować dwie liczby od siebie.
          Dla danego wyrażenia obliczasz jego różnicę. Obliczanie różnicy to zabieranie z liczby jakiejś liczby. Na przykład
          4 - 7 = 4 zabierz 7, otrzymujemy po kolei 3,2,1,0,-1,-2,-3. Wynik to -3.         
        <</SYS>>
        [INST] Policz mi podane wyrażenie: 2 - 2[/INST]
        0
        [INST] Policz mi podane wyrażenie: 1 - 5[/INST]
        -4
        [INST] Policz mi podane wyrażenie: 7 - 8[/INST]
        -1
        [INST] Policz mi podane wyrażenie: 6 - 0[/INST]
        3
        [INST] Policz mi podane wurażenie: 8 - 1[/INST]
        7
        [INST] Policz mi podane wyrażenie: 9 - 8[/INST]
        1
        [INST] Policz mi podane wyrażenie: {n1} - {n2}[/INST]
        """,

    "substraction_rigid": """3 - 4 = -1
    5 - 4 = 1
    3 - 9 = -6
    8 - 0 = 8
    1 - 8 = -7
    {n1} - {n2} = """
}


# dla liczb całkowitych, dodatnich
MULTIPLICATION = {
    "multiplication_one_digit": """
        <s><<SYS>>Jesteś prostym kalkulatorem, który jest w stanie mnożyć dwie liczby przez siebie. 
        Dla danego wyrażenia obliczasz jego iloczyn. Maksymalna wartość, jaką możesz otrzymać to 81!
        <</SYS>>
        [INST] Policz mi podane wyrażenie: 3 * 2[/INST]
        6
        [INST] Policz mi podane wyrażenie: 2 * 3[/INST]
        6
        [INST] Policz mi podane wyrażenie: 7 * 8[/INST]
        56
        [INST] Policz mi podane wyrażenie: 9 * 4[/INST]
        36
        [INST] Policz mi podane wyrażenie: 6 * 0[/INST]
        0
        [INST] Policz mi podane wyrażenie: 0 * 1[/INST]
        0
        [INST] Policz mi podane wyrażenie: {n1} * {n2}[/INST]
        """,
    
    "multiplication_rigid":"""2 * 1 = 2
    1 * 4 = 4
    4 * 6 = 24
    8 * 8 = 64
    0 * 9 = 0
    8 * 0 = 0
    {n1} * {n2} =""",

    "multiplication_table":"""Jesteś maszyną, która ma za zadanie znaleźć iloczyn dwóch liczb w tabelce mnożenia. Oto jak powinieneś to zrobić:

1. Zobacz dwie liczby, które masz pomnożyć (w tym przypadku {n1} i {n2})
2. Pierwszą liczbę ({n1}) traktuj jako numer wiersza
3. Drugą liczbę ({n2}) traktuj jako numer kolumny
4. Znajdź miejsce, gdzie przecina się wiersz {n1} z kolumną {n2}
5. Odczytaj liczbę z tego miejsca - to będzie wynik mnożenia

Patrząc na tabelkę:
- Idź do wiersza {n1} (liczysz od góry).
- W tym wierszu idź do kolumny {n2} (liczysz od lewej).
- W miejscu przecięcia znajduje się liczba.
- To jest wynik mnożenia {n1} * {n2}

Odpowiedź:"""
}

# dla liczb całkowitych, dodatnich
DIVISION = {
    "division_one_digit": """
        <s><<SYS>>Jesteś prostym kalkulatorem, który jest w stanie dzielić dwie liczby przez siebie. 
        Dla danego wyrażenia obliczasz jego iloraz. MINIMALNA wartość, jaką możesz otrzymać to 0, MAKSYMALNA wartość to 9!
        <</SYS>>
        [INST] Policz mi podane wyrażenie: 6 / 1[/INST]
        6
        [INST] Policz mi podane wyrażenie: 8 / 3[/INST]
        2
        [INST] Policz mi podane wyrażenie: 9 / 4[/INST]
        2
        [INST] Policz mi podane wyrażenie: 7 / 4[/INST]
        1
        [INST] Policz mi podane wyrażenie: 8 / 8[/INST]
        1
        [INST] Policz mi podane wyrażenie: 1 / 3[/INST]
        0
        [INST] Policz mi podane wyrażenie: {n1} / {n2}[/INST]
        """,
}

OP_MAP = {
        "+": lambda x,y : x + y,
        "-": lambda x,y: x - y,
        "*": lambda x,y: x * y,
        "/": lambda x,y: x // y
    }


def create_programatic_text_prompt(operation: str, rg: tuple, n: int) -> Tuple[str, int, int]:
    arg1, arg2 = random.randint(rg[0], rg[1]), random.randint(rg[0], rg[1])
    
    prompt = f"instruction: Compute {arg1} {operation} {arg2},\ninput: {arg1}, {operation}, {arg2},\noutput: "

    return prompt, arg1, arg2


def create_few_shot_text_prompt(operation: str, rg: tuple, n: int) -> Tuple[str, int, int]:
    prompt = """<s><<SYS>>Jesteś prostym kalkulatorem, który jest w stanie robić proste obliczenia. 
        Twoim jedynym życiowym celem jest policzenie właściwego wyniku działania arytmetycznego!<</SYS>>"""
    
    for _ in range(n):
        arg1, arg2 = random.randint(rg[0], rg[1]), random.randint(rg[0], rg[1])

        prompt = f"{prompt}\n[INST] Policz mi wyrażenie: {arg1} {operation} {arg2}[/INST]\n={OP_MAP[operation](arg1, arg2)}"

    arg1, arg2 = random.randint(rg[0], rg[1]), random.randint(rg[0], rg[1])
    prompt = f"{prompt}\n[INST] Policz mi wyrażenie: {arg1} {operation} {arg2}[/INST]\n="

    return prompt, arg1, arg2




def create_rigid_propmt(operation: str, rg: tuple, n: int) -> Tuple[str, int, int]:
    """
        operation - operacja
        rg - zakres liczbowy
        n - liczba przykładów
    """
    prompt = ""

    for _ in range(n):
        n1, n2 = random.randint(rg[0], rg[1]), random.randint(rg[0], rg[1])
        prompt += f"{n1} {operation} {n2} = {OP_MAP[operation](n1, n2)}\n"
    arg1, arg2 = random.randint(1,10), random.randint(1,10)
    prompt += f"{arg1} {operation} {arg2} = "
    return prompt, arg1, arg2

def get_prompt(prompt_type: str, complexity: str, n1: int, n2: int):

    prompts_map = {
        "addition": ADDITION,
        "substraction": SUBSTRACTION,
        "multiplication": MULTIPLICATION,
        "division": DIVISION
    }

    if prompt_type not in prompts_map:
        raise ValueError(f"Invalid prompt_type")
    
    return prompts_map[prompt_type][complexity].format(n1=n1, n2=n2)
