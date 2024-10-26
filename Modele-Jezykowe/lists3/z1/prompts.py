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
    
    "addition_two_digits": """
       <s><<SYS>>Jesteś pomocnym asystentem matematycznym. Twoim zadaniem jest dodawanie dwóch liczb dwucyfrowych do siebie. Przeanalizuj poniższe przykłady, a następnie rozwiąż nowe zadanie w ten sam sposób.<</SYS>>

        Przykład 1:
        [INST]Pytanie: Dodaj liczby 23 i 45[/INST]
        Myślenie: 
        1. Najpierw dodaję cyfry jednostek: 3 + 5 = 8
        2. Następnie dodaję cyfry dziesiątek: 2 + 4 = 6
        3. Łączę wyniki: 68
        Odpowiedź: 23 + 45 = 68

        Przykład 2:
        [INST]Pytanie: Dodaj liczby 78 i 91[/INST]
        Myślenie:
        1. Najpierw dodaję cyfry jednostek: 8 + 1 = 9
        2. Następnie dodaję cyfry dziesiątek: 7 + 9 = 16
        3. Ponieważ suma dziesiątek jest większa niż 9, zapisuję 6 w dziesiątkach, a 1 przenoszę do setek
        4. Dodaję przeniesioną 1 do wyniku: 169
        Odpowiedź: 78 + 91 = 169

        Przykład 3:
        [INST]Pytanie: Dodaj liczby 52 i 37[/INST]
        Myślenie:
        1. Najpierw dodaję cyfry jednostek: 2 + 7 = 9
        2. Następnie dodaję cyfry dziesiątek: 5 + 3 = 8
        3. Łączę wyniki: 89
        Odpowiedź: 52 + 37 = 89

        [INST]Teraz twoja kolej. Dodaj następujące liczby: {n1} i {n2}
        Pamiętaj, aby pokazać swoje myślenie krok po kroku.[/INST]
    """
}

SUBSTRACTION = {
    "substraction_one_digit": """
        <s><<SYS>>Jesteś prostym kalkulatorem, który jest w stanie dodawać dwie liczby do siebie. Dla danego wyrażenia obliczasz jego sumę.<</SYS>>
        [INST] Policz mi podane wyrażenie: 2 - 2[/INST]
        0
        [INST] Policz mi podane wyrażenie: 1 - 5[/INST]
        -4
        [INST] Policz mi podane wyrażenie: 7 - 8[/INST]
        -1
        [INST] Policz mi podane wyrażenie: 9 - 8[/INST]
        1
        [INST] Policz mi podane wyrażenie: {n1} - {n2}[/INST]
        """,
}
# dla liczb całkowitych, dodatnich
MULTIPLICATION = {
    "multiplication_one_digit": """
        <s><<SYS>>Jesteś prostym kalkulatorem, który jest w stanie dodawać dwie liczby do siebie. 
        Dla danego wyrażenia obliczasz jego sumę. Maksymalna wartość, jaką możesz otrzymać to 100!
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
}

# dla liczb całkowitych, dodatnich
DIVISION = {
    "division_one_digit": """
        <s><<SYS>>Jesteś prostym kalkulatorem, który jest w stanie dodawać dwie liczby do siebie. 
        Dla danego wyrażenia obliczasz jego sumę. Maksymalna wartość, jaką możesz otrzymać to 100!
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
}

DIVISION = {
    "division_one_digit": """
        <s><<SYS>>Jesteś prostym kalkulatorem, który jest w stanie dodawać dwie liczby do siebie. 
        Dla danego wyrażenia obliczasz jego sumę. MINIMALNA wartość, jaką możesz otrzymać to 1!
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
