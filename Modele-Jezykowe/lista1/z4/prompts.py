import random
from typing import List
# Zero-shot prompts for each category
ZERO_SHOT_PROMPTS = {
    "czy": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>

    [INST]Odpowiedz "tak" lub "nie" na następujące pytanie.[/INST]

### Pytanie:
{question}

### Odpowiedź: """,

    "czy_opt": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>

    [INST]Wybierz jedną z opcji podanych w pytaniu. Opcja w pytaniu do sformułowanie leżące na lewo od słowa 'czy'
    albo na prawo od niego.[/INST]

### Pytanie:
{question}

### Odpowiedź: """,

    "jak+": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
[INST] Odpowiedz krótko na pytanie zaczynające się od "jak". Odpowiedź powinna być RZECZOWNIKIEM[/INST]

### Pytanie:
{question}

### Odpowiedź: """,

    "ile": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>

    [INST]Podaj wartość liczbową w odpowiedzi na pytanie.[/INST]

### Pytanie:
{question}

### Odpowiedź: """,

    "w_ktorym+": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
[INST]Podaj dokładną datę, okres lub miejsce.[/INST]

### Pytanie:
{question}

### Odpowiedź: """,

    "kto": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
[INST]Podaj imię i/lub nazwisko osoby.[/INST]

### Pytanie:
{question}


### Odpowiedź: """,

    "rest": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
[INST]Odpowiedz krótko i precyzyjnie na pytanie.[/INST]

### Pytanie:
{question}

### Odpowiedź: """
}

# One-shot prompts for each category
ONE_SHOT_PROMPTS = {
    "czy": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania.
    Pytania są z kategorii "tak" lub "nie"<</SYS>>
[INST]Odpowiedz "tak" lub "nie" na następujące pytanie.[/INST]
[INST]Czy Ziemia krąży wokół Słońca?[/INST]
tak
[INST] Odpowiedz "tak" lub "nie" na następujące pytanie.[/INST]
[INST]{question}[/INST]
""",

    "czy_opt":"""<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
    [INST]Wybierz jedną z opcji podanych w pytaniu. Opcja w pytaniu do sformułowanie leżące na lewo od słowa 'czy'
    albo na prawo od niego.[/INST]
    [INST]Czy Warszawa leży nad Wisłą czy nad Odrą?[/INST]
    nad Wisłą
    [INST]{question}[/INST]""",

    "jak+": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
[INST] Odpowiedz krótko na pytanie zaczynające się od "jak". Odpowiedź powinna być RZECZOWNIKIEM[/INST]
[INST]Jak nazywa się najwyższy szczyt Polski?[/INST]
Rysy
[INST]{question}[/INST]""",

    "ile": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
    [INST]Podaj wartość liczbową w odpowiedzi na pytanie.[/INST]
[INST]Ile województw jest w Polsce?[/INST]
16
[INST]{question}[/INST]""",

    "w_ktorym+": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
[INST]Podaj dokładną datę, okres lub miejsce.[/INST]
[INST]W którym roku Polska wstąpiła do Unii Europejskiej?[/INST]
2004
[INST]{question}[/INST]]""",

    "kto": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
[INST]Podaj imię i/lub nazwisko osoby.[/INST]
[INST]Kto jest autorem "Quo Vadis"?[/INST]
Henryk Sienkiewicz
[INST]{question}[/INST]""",

    "rest": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
[INST]Odpowiedz krótko i precyzyjnie na pytanie.[/INST]
[INST]Co jest stolicą Polski?[/INST]
Warszawa
[INST]{question}[/INST]"""
}

# Few-shot prompts for each category
FEW_SHOT_PROMPTS = {
    "czy": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania.
    Pytania są z kategorii "tak" lub "nie"<</SYS>>
[INST]Odpowiedz "tak" lub "nie" na następujące pytanie.[/INST]
### Pytanie:
Czy Słońce jest gwiazdą?
### Odpowiedź:
tak
[INST] Odpowiedz "tak" lub "nie" na następujące pytanie.[/INST]
### Pytanie:
Czy Ziemia jest płaska?
### Odpowiedź:
nie
[INST] Odpowiedz "tak" lub "nie" na następujące pytanie.[/INST]
### Pytanie:
Czy woda wrze w temperaturze 100 stopni Celsjusza?
### Odpowiedź:
tak
[INST] Odpowiedz "tak" lub "nie" na następujące pytanie.[/INST]
### Pytanie:
{question}
### Odpowiedź:
""",

    "czy_opt": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
    [INST]Wybierz jedną z opcji podanych w pytaniu. Opcja w pytaniu do sformułowanie leżące na lewo od słowa 'czy'
    albo na prawo od niego.[/INST]
    [INST] Odpowiedz jedną z opcji na następujące pytanie.[/INST]
    ### Pytanie:
    Czy Księżyc jest naturalnym satelitą Ziemi czy Marsa?
    ### Odpowiedź:
    naturalnym satelitą Ziemi
    [INST] Odpowiedz jedną z opcji na następujące pytanie.[/INST]
    ### Pytanie:
    Czy złoto jest metalem szlachetnym czy nieszlachetnym?
    ### Odpowiedź:
    metalem szlachetnym
    [INST] Odpowiedz jedną z opcji na następujące pytanie.[/INST]    
    ### Pytanie:
    Czy delfin jest rybą czy ssakiem?
    ### Odpowiedź:
    ssakiem
    [INST] Odpowiedz jedną z opcji na następujące pytanie.[/INST]
    ### Pytanie:
    {question}
    ### Odpowiedź:
    """,

    "jak+": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
    [INST] Odpowiedz krótko na pytanie zaczynające się od "jak". Odpowiedź powinna być RZECZOWNIKIEM[/INST]
    ### Pytanie:
    Jak nazywa się stolica Francji?
    ### Odpowiedź:
    Paryż
    [INST] Odpowiedz krótko na pytanie zaczynające się od "jak". Odpowiedź powinna być RZECZOWNIKIEM[/INST]
    ### Pytanie:
    Jak nazywa się największy kontynent?
    ### Odpowiedź:
    Azja
    [INST] Odpowiedz krótko na pytanie zaczynające się od "jak". Odpowiedź powinna być RZECZOWNIKIEM[/INST]
    ### Pytanie:
    Jak nazywa się naturalne satelita Ziemi?
    ### Odpowiedź:
    Księżyc
    [INST] Odpowiedz krótko na pytanie zaczynające się od "jak". Odpowiedź powinna być RZECZOWNIKIEM[/INST]
    ### Pytanie:
    {question}
    ### Odpowiedź:""",

    "ile": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
    [INST]Podaj wartość liczbową w odpowiedzi na pytanie.[/INST]
    ### Pytanie:
    Ile dni ma tydzień?
    ### Odpowiedź:
    7
    ### Pytanie:
    Ile kontynentów jest na Ziemi?
    ### Odpowiedź:
    7
    ### Pytanie:
    Ile wynosi pierwiastek kwadratowy z 16?
    ### Odpowiedź:
    4
    ### Pytanie:
    {question}
    ### Odpowiedź:
    """,

    "w_ktorym+": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
    [INST]Podaj dokładną datę, okres lub miejsce.[/INST]
    ### Pytanie:
    W którym mieście znajduje się wieża Eiffla?
    ### Odpowiedź:
    w Paryżu
    ### Pytanie:
    W którym wieku wynaleziono druk?
    ### Odpowiedź:
    w XV wieku
    ### Pytanie:
    W którym miesiącu rozpoczyna się kalendarzowa wiosna?
    ### Odpowiedź:
    w marcu
    ### Pytanie:
    {question}
    ### Odpowiedź:
    """,

    "kto": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
[INST]Podaj imię i/lub nazwisko osoby.[/INST]
### Pytanie:
Kto napisał "Pan Tadeusz"?
### Odpowiedź:
Adam Mickiewicz
### Pytanie:
Kto odkrył Amerykę?
### Odpowiedź:
Krzysztof Kolumb
### Pytanie:
Kto jest autorem teorii względności?
### Odpowiedź:
Albert Einstein
### Pytanie:
{question}
### Odpowiedź:
""",

    "rest": """<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
    [INST]Odpowiedz krótko i precyzyjnie na pytanie.[/INST]
    ### Pytanie:
    Który pierwiastek chemiczny jest najlżejszy?
    ### Odpowiedź:
    wodór
    ### Pytanie:
    Z którego kraju pochodzi pizza?
    ### Odpowiedź:
    z Włoch
    ### Pytanie:
    Która planeta jest najbliżej Słońca?
    ### Odpowiedź:
    Merkury
    ### Pytanie:
    {question}
    ### Odpowiedź:"""
}

# each question is a tuple question, [answers]
def create_propmpt(question: str, questions: List[tuple], category: str, prompt_type: str = "zero") -> str:
    
    if category == "czy":
        prompt = "<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem odpowiadać na pytania używając tylko TAK i NIE<</SYS>>\n"
        if prompt_type == "one":
            q = random.randint(0, len(question))
            prompt = f"""{prompt}[INST]Odpowiedz używając TAK lub NIE na następujące pytanie.[/INST]\n[INST]{questions[q][0]}[/INST]\n{questions[q][1][0]}\n"""
        elif prompt_type == "few":
            idxs = [random.randint(0, len(question)) for _ in range(5)]
            for i in idxs:
                prompt = f"""{prompt}[INST]Odpowiedz TAK lub NIE na pytanie.[/INST]\n[INST]{questions[i][0]}[/INST]\n{questions[i][1][0]}\n"""

        prompt = f"""{prompt}[INST]Odpowiedz TAK lub NIE na pytanie.[/INST]\n[INST]{question}[/INST]\n"""
    elif category == "czy_opt":
        prompt = """<s><<SYS>>Jesteś uczestnikiem quizu. Odpowiadaj na pytania wybierając jedno z wyrażeń obok "czy"<</SYS>>\n"""
        if prompt_type == "one":
            q = random.randint(0, len(questions)-1)
            prompt = f"""{prompt}[INST]Wybierz jedną odpowiedź, z podanych w pytaniu opcji.[/INST]\n[INST]{questions[q][0]}[/INST]\n{questions[q][1][0]}\n"""
        elif prompt_type == "few":
            idxs = [random.randint(0, len(questions)-1) for _ in range(5)]
            for i in idxs:
                prompt = f"""{prompt}\n[INST]{questions[i][0]}[/INST]\n{questions[i][1][0]}\n"""
        prompt = f"""{prompt}[INST]Wybierz jedną odpowiedź, z podanych w pytaniu opcji.[/INST]\n[INST]{question}[/INST]\n"""
    
    elif category  == "jak+":
        prompt = "<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest odpowiadać na pytania jakimś jednym słowem<</SYS>>\n"
        if prompt_type == "one":
            q = random.randint(0, len(questions)-1)
            prompt = f"""{prompt}[INST]Odpowiedz jednym słowem na pytanie.[/INST]\n[INST]{questions[q][0]}[/INST]\n{questions[q][1][0]}\n"""
        elif prompt_type == "few":
            idxs = [random.randint(0, len(questions)-1) for _ in range(5)]
            for i in idxs:
                prompt = f"""{prompt}[INST]Odpowiedz jednym słowem na pytanie.[/INST]\n[INST]{questions[i][0]}[/INST]\n{questions[i][1][0]}\n"""
        prompt = f"""{prompt}[INST]Odpowiedz jednym słowem na pytanie.[/INST]\n[INST]{question}[/INST]\n"""
    
    elif category == "ile":
        prompt = "<s><<SYS>>Jesteś uczestnikiem quizu. Podaj wartość liczbową w odpowiedzi na pytanie.<</SYS>>\n"
        if prompt_type == "one":
            q = random.randint(0, len(questions)-1)
            prompt = f"""{prompt}[INST]Odpowiedz podając liczbę.[/INST]\n[INST]{questions[q][0]}[/INST]\nOdpowiedź: {questions[q][1][0]}\n"""
        elif prompt_type == "few":
            idxs = [random.randint(0, len(questions)-1) for _ in range(5)]
            for i in idxs:
                prompt = f"""{prompt}[INST]Odpowiedz podając liczbę.[/INST]\n[INST]{questions[i][0]}[/INST]\n{questions[i][1][0]}\n"""
        prompt = f"""{prompt}[INST]Odpowiedz podając liczbę.[/INST]\n[INST]{question}[/INST]\nOdpowiedź: """
    
    elif category == "kto":
        prompt = "<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest odpowiadać imieniem i nazwiskiem lub nazwą na zadane pytania.<</SYS>>\n"
        if prompt_type == "one":
            q = random.randint(0, len(questions)-1)
            prompt = f"""{prompt}[INST]Odpowiedz podając imię i nazwisko lub nazwę.[/INST]\n[INST]{questions[q][0]}[/INST]\n{questions[q][1][0]}\n"""
        elif prompt_type == "few":
            idxs = [random.randint(0, len(questions)-1) for _ in range(5)]
            for i in idxs:
                prompt = f"""{prompt}[INST]Odpowiedz podając imię i nazwisko lub nazwę.[/INST]\n[INST]{questions[i][0]}[/INST]\n{questions[i][1][0]}\n"""
        prompt = f"""{prompt}[INST]Odpowiedz podając imię i nazwisko lub nazwę.[/INST]\n[INST]{question}[/INST]\n"""

    elif category == "w_którym+":
        prompt = "<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest odpowiadać podając dokładną datę, okres lub miejsce.<</SYS>>\n"
        if prompt_type == "one":
            q = random.randint(0, len(questions)-1)
            prompt = f"""{prompt}[INST]Odpowiedz podając datę, okres lub miejsce.[/INST]\n[INST]{questions[q][0]}[/INST]\nOdpowiedź: {questions[q][1][0]}\n"""
        elif prompt_type == "few":
            idxs = [random.randint(0, len(questions)-1) for _ in range(5)]
            for i in idxs:
                prompt = f"""{prompt}[INST]Odpowiedz podając datę, okres lub miejsce.[/INST]\n[INST]{questions[i][0]}[/INST]\n{questions[i][1][0]}\n"""
        prompt = f"""{prompt}[INST]Odpowiedz podając datę, okres lub miejsce.[/INST]\n[INST]{question}[/INST]\nOdpowiedź: """
    
    else:  # category == "rest"
        prompt = "<s><<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest odpowiadać krótko i zwięźle na zadane pytania.<</SYS>>\n"
        if prompt_type == "one":
            q = random.randint(0, len(questions)-1)
            prompt = f"""{prompt}[INST]Odpowiedz krótko i zwięźle.[/INST]\n[INST]{questions[q][0]}[/INST]\n{questions[q][1][0]}\n"""
        elif prompt_type == "few":
            idxs = [random.randint(0, len(questions)-1) for _ in range(5)]
            for i in idxs:
                prompt = f"""{prompt}[INST]Odpowiedz krótko i zwięźle.[/INST]\n[INST]{questions[i][0]}[/INST]\n{questions[i][1][0]}\n"""
        prompt = f"""{prompt}[INST]Odpowiedz krótko i zwięźle.[/INST]\n[INST]{question}[/INST]\n"""
    
    return prompt

def get_prompt(question: str, category: str, prompt_type: str = "zero") -> str:
    """
    Get formatted prompt for given question and category.
    
    Args:
        question: Question to ask
        category: Category of the question ('czy', 'czy_opt', etc.)
        prompt_type: Type of prompt to use ('zero', 'one', or 'few')
    
    Returns:
        Formatted prompt string
    """
    prompt_maps = {
        "zero": ZERO_SHOT_PROMPTS,
        "one": ONE_SHOT_PROMPTS,
        "few": FEW_SHOT_PROMPTS
    }
    
    if prompt_type not in prompt_maps:
        raise ValueError(f"Invalid prompt_type. Must be one of: {', '.join(prompt_maps.keys())}")
        
    return prompt_maps[prompt_type][category].format(question=question)
