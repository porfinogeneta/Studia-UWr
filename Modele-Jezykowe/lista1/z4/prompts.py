# Zero-shot prompts for each category
ZERO_SHOT_PROMPTS = {
    "czy": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Odpowiedz "tak" lub "nie" na następujące pytanie.

### Pytanie:
{question}

### Odpowiedź: [/INST]""",

    "czy_opt": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Wybierz jedną z opcji podanych w pytaniu, opcja to element po lewej i prawej stronie słowa 'czy'.

### Pytanie:
{question}

### Odpowiedź: [/INST]""",

    "jak+": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Odpowiedz krótko na pytanie zaczynające się od "jak".

### Pytanie:
{question}

### Odpowiedź: [/INST]""",

    "ile": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Podaj wartość liczbową w odpowiedzi na pytanie.

### Pytanie:
{question}

### Odpowiedź: [/INST]""",

    "w_ktorym+": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Podaj dokładną datę lub okres.

### Pytanie:
{question}

### Odpowiedź: [/INST]""",

    "kto": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Podaj imię i/lub nazwisko osoby.

### Pytanie:
{question}


### Odpowiedź: [/INST]""",

    "rest": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Odpowiedz krótko i precyzyjnie na pytanie.

### Pytanie:
{question}

### Odpowiedź: [/INST]"""
}

# One-shot prompts for each category
ONE_SHOT_PROMPTS = {
    "czy": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Odpowiedz "tak" lub "nie" na następujące pytanie.
### Pytanie:
Czy Ziemia krąży wokół Słońca?
### Odpowiedź: [/INST]
tak
<s>[INST] Odpowiedz "tak" lub "nie" na następujące pytanie.
### Pytanie:
{question}
### Odpowiedź: [/INST]""",

    "czy_opt": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Wybierz jedną z opcji podanych w pytaniu, opcja to element po lewej i prawej stronie słowa 'czy'.
### Pytanie:
Czy Warszawa leży nad Wisłą czy nad Odrą?
### Odpowiedź: [/INST]
nad Wisłą
<s>[INST] Wybierz jedną z opcji podanych w pytaniu, opcja to element po lewej i prawej stronie słowa 'czy'.
### Pytanie:
{question}
### Odpowiedź: [/INST]""",

    "jak+": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Odpowiedz krótko na pytanie zaczynające się od "jak".
### Pytanie:
Jak nazywa się najwyższy szczyt Polski?
### Odpowiedź: [/INST]
Rysy
<s>[INST] Odpowiedz krótko na pytanie zaczynające się od "jak".
### Pytanie:
{question}
### Odpowiedź: [/INST]""",

    "ile": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Podaj wartość liczbową w odpowiedzi na pytanie.
### Pytanie:
Ile województw jest w Polsce?
### Odpowiedź: [/INST]
16
<s>[INST] Podaj wartość liczbową w odpowiedzi na pytanie.
### Pytanie:
{question}
### Odpowiedź: [/INST]""",

    "w_ktorym+": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Podaj dokładną datę lub okres.
### Pytanie:
W którym roku Polska wstąpiła do Unii Europejskiej?
### Odpowiedź: [/INST]
2004
<s>[INST] Podaj dokładną datę lub okres.
### Pytanie:
{question}
### Odpowiedź: [/INST]""",

    "kto": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Podaj imię i/lub nazwisko osoby.
### Pytanie:
Kto jest autorem "Quo Vadis"?
### Odpowiedź: [/INST]
Henryk Sienkiewicz
<s>[INST] Podaj imię i/lub nazwisko osoby.
### Pytanie:
{question}
### Odpowiedź: [/INST]""",

    "rest": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Odpowiedz krótko i precyzyjnie na pytanie.
### Pytanie:
Co jest stolicą Polski?
### Odpowiedź: [/INST]
Warszawa
<s>[INST] Odpowiedz krótko i precyzyjnie na pytanie.
### Pytanie:
{question}
### Odpowiedź: [/INST]"""
}

# Few-shot prompts for each category
FEW_SHOT_PROMPTS = {
    "czy": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Odpowiedz "tak" lub "nie" na następujące pytanie.
### Pytanie:
Czy Słońce jest gwiazdą?
### Odpowiedź: [/INST]
tak
<s>[INST] Odpowiedz "tak" lub "nie" na następujące pytanie.
### Pytanie:
Czy Ziemia jest płaska?
### Odpowiedź: [/INST]
nie
<s>[INST] Odpowiedz "tak" lub "nie" na następujące pytanie.
### Pytanie:
Czy woda wrze w temperaturze 100 stopni Celsjusza?
### Odpowiedź: [/INST]
tak
<s>[INST] Odpowiedz "tak" lub "nie" na następujące pytanie.
### Pytanie:
{question}
### Odpowiedź: [/INST]""",

    "czy_opt": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Wybierz jedną z opcji podanych w pytaniu, opcja to element po lewej i prawej stronie słowa 'czy'.
### Pytanie:
Czy Księżyc jest naturalnym satelitą Ziemi czy Marsa?
### Odpowiedź: [/INST]
naturalnym satelitą Ziemi
<s>[INST] Wybierz jedną z opcji podanych w pytaniu, opcja to element po lewej i prawej stronie słowa 'czy'.
### Pytanie:
Czy złoto jest metalem szlachetnym czy nieszlachetnym?
### Odpowiedź: [/INST]
metalem szlachetnym
<s>[INST] Wybierz jedną z opcji podanych w pytaniu, opcja to element po lewej i prawej stronie słowa 'czy'.
### Pytanie:
Czy delfin jest rybą czy ssakiem?
### Odpowiedź: [/INST]
ssakiem
<s>[INST] Wybierz jedną z opcji podanych w pytaniu, opcja to element po lewej i prawej stronie słowa 'czy'.
### Pytanie:
{question}
### Odpowiedź: [/INST]""",

    "jak+": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Odpowiedz krótko na pytanie zaczynające się od "jak".
### Pytanie:
Jak nazywa się stolica Francji?
### Odpowiedź: [/INST]
Paryż
<s>[INST] Odpowiedz krótko na pytanie zaczynające się od "jak".
### Pytanie:
Jak nazywa się największy kontynent?
### Odpowiedź: [/INST]
Azja
<s>[INST] Odpowiedz krótko na pytanie zaczynające się od "jak".
### Pytanie:
Jak nazywa się naturalne satelita Ziemi?
### Odpowiedź: [/INST]
Księżyc
<s>[INST] Odpowiedz krótko na pytanie zaczynające się od "jak".
### Pytanie:
{question}
### Odpowiedź: [/INST]""",

    "ile": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Podaj wartość liczbową w odpowiedzi na pytanie.
### Pytanie:
Ile dni ma tydzień?
### Odpowiedź: [/INST]
7
<s>[INST] Podaj wartość liczbową w odpowiedzi na pytanie.
### Pytanie:
Ile kontynentów jest na Ziemi?
### Odpowiedź: [/INST]
7
<s>[INST] Podaj wartość liczbową w odpowiedzi na pytanie.
### Pytanie:
Ile wynosi pierwiastek kwadratowy z 16?
### Odpowiedź: [/INST]
4
<s>[INST] Podaj wartość liczbową w odpowiedzi na pytanie.
### Pytanie:
{question}
### Odpowiedź: [/INST]""",

    "w_ktorym+": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Podaj dokładną datę lub okres.
### Pytanie:
W którym mieście znajduje się wieża Eiffla?
### Odpowiedź: [/INST]
w Paryżu
<s>[INST] Podaj dokładną datę lub okres.
### Pytanie:
W którym wieku wynaleziono druk?
### Odpowiedź: [/INST]
w XV wieku
<s>[INST] Podaj dokładną datę lub okres.
### Pytanie:
W którym miesiącu rozpoczyna się kalendarzowa wiosna?
### Odpowiedź: [/INST]
w marcu
<s>[INST] Podaj dokładną datę lub okres.
### Pytanie:
{question}
### Odpowiedź: [/INST]""",

    "kto": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Podaj imię i/lub nazwisko osoby.
### Pytanie:
Kto napisał "Pan Tadeusz"?
### Odpowiedź: [/INST]
Adam Mickiewicz
<s>[INST] Podaj imię i/lub nazwisko osoby.
### Pytanie:
Kto odkrył Amerykę?
### Odpowiedź: [/INST]
Krzysztof Kolumb
<s>[INST] Podaj imię i/lub nazwisko osoby.
### Pytanie:
Kto jest autorem teorii względności?
### Odpowiedź: [/INST]
Albert Einstein
<s>[INST] Podaj imię i/lub nazwisko osoby.
### Pytanie:
{question}
### Odpowiedź: [/INST]""",

    "rest": """<s>[INST] <<SYS>>Jesteś uczestnikiem quizu. Twoim zadaniem jest w prostych słowach odpowiadać na pytania<</SYS>>
Odpowiedz krótko i precyzyjnie na pytanie.
### Pytanie:
Który pierwiastek chemiczny jest najlżejszy?
### Odpowiedź: [/INST]
wodór
<s>[INST] Odpowiedz krótko i precyzyjnie na pytanie.
### Pytanie:
Z którego kraju pochodzi pizza?
### Odpowiedź: [/INST]
z Włoch
<s>[INST] Odpowiedz krótko i precyzyjnie na pytanie.
### Pytanie:
Która planeta jest najbliżej Słońca?
### Odpowiedź: [/INST]
Merkury
<s>[INST] Odpowiedz krótko i precyzyjnie na pytanie.
### Pytanie:
{question}
### Odpowiedź: [/INST]"""
}


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
