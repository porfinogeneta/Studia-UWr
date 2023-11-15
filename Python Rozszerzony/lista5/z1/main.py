# wyjątki
class LackingVariableAssignment(Exception):
    def __init__(self, message):
        self.message = message

class InvalidVariableAssignment(Exception):
    def __init__(self, message):
        self.message = message

class Formula:
    def evaluate(self, variables):
        pass

    def __str__(self):
        pass

    def __add__(self, f1):
        return Or(self, f1)

    def __mul__(self, f1):
        return And(self, f1)

    def getFreeVars(self):
        if isinstance(self, Or) or isinstance(self, And):
            # robimy unię dwóch zbiorów
            return self.left_fi.getFreeVars() | self.right_fi.getFreeVars()
        elif isinstance(self, Not):
            return self.sub_fi.getFreeVars()
        elif isinstance(self, Variable):
            return {self.var_name}
        return set()

    # kolejne wartościowania T/F można uzyskać przez badanie zapalonych bitów
    # w ciągach 2^n - 1, gdzie n to długość zbioru zmiennych
    # 1 w zapisie bitowym oznacza True, 0 - False
    def tautology(self):
        n = len(self.getFreeVars())
        # robimy słownik postaci {'zmienna' przykładowe wartościowanie}
        frvars = list(self.getFreeVars())
        vars_dict = {element: False for element in self.getFreeVars()}
        for b in range(n**2):
            # będziemy używać n bitów - liczba bitów to dł zbioru
            for j in range(n):
                # sprawdzamy czy kolejne bity z liczb są zapalone
                if ((b >> j) & 1) == 1:
                    vars_dict[frvars[j-1]] = True # idąc od tyłu zmieniamy dla zapalonych bitów na True

            # jak dostaniemy False dla jakiegoś wartościowania to nie może to być tautologia
            if not self.evaluate(vars_dict):
                return False
            # resetujemy nasz słownik przed kolejną iteracją
            vars_dict = {element: False for element in self.getFreeVars()}
        # jak jest tautologią zwracam po prostu True
        return True

    def simplify(self):
        pass

class Or(Formula):
    def __init__(self, left_fi, right_fi):
        self.left_fi = left_fi
        self.right_fi = right_fi

    # obliczamy lewą i prawą gałąź
    def evaluate(self, variables):
        return self.left_fi.evaluate(variables) or self.right_fi.evaluate(variables)

    def __str__(self):
        return f"({self.left_fi} ∨ {self.right_fi})"

    # uproszeczenie OR false ∨ p ≡ p
    def simplify(self):
        left_simplified = self.left_fi.simplify()
        right_simplified = self.right_fi.simplify()
        if isinstance(left_simplified, Constant) and left_simplified.value == False:
            return right_simplified
        elif isinstance(right_simplified, Constant) and right_simplified.value == False:
            return left_simplified
        else:
            return Or(left_simplified, right_simplified)

class And(Formula):
    def __init__(self, left_fi, right_fi):
        self.left_fi = left_fi
        self.right_fi = right_fi

    def evaluate(self, variables):
        return self.left_fi.evaluate(variables) and self.right_fi.evaluate(variables)

    def __str__(self):
        return f"({self.left_fi} ∧ {self.right_fi})"

    def simplify(self):
        left_simplified = self.left_fi.simplify()
        right_simplified = self.right_fi.simplify()
        if isinstance(left_simplified, Constant) and left_simplified.value == False:
            return Constant(False)
        elif isinstance(right_simplified, Constant) and right_simplified.value == False:
            return Constant(False)
        else:
            return And(left_simplified, right_simplified)


class Not(Formula):
    def __init__(self, sub_fi):
        self.sub_fi = sub_fi

    def evaluate(self, variables):
        return not self.sub_fi.evaluate(variables)

    def __str__(self):
        return f"¬({self.sub_fi})"

    def simplify(self):
        return Not(self.sub_fi.simplify())


class Variable(Formula):
    def __init__(self, var_name):
        self.var_name = var_name

    # pobieramy wartość zmiennej ze słownika
    def evaluate(self, variables):
        if self.var_name not in variables:
            raise LackingVariableAssignment('No assignment to variable!')
        value = variables.get(self.var_name)
        if not isinstance(value, bool):
            raise InvalidVariableAssignment('Invalid variable type!')
        return variables.get(self.var_name)

    def __str__(self):
        return f"{self.var_name}"

    def simplify(self):
        return Variable(self.var_name)

class Constant(Formula):
    def __init__(self, value):
        self.value = value

    # dla stałej to po prostu zwrócenie jej wartośći
    def evaluate(self, variables):
        return self.value

    def __str__(self):
        return f"{self.value}"

    def simplify(self):
        return Constant(self.value)

if __name__ == '__main__':
    fi = Or(Not(Variable("x")), And(Variable("y"), Constant(True)))
    var_dict = {"x": False, "y": False}
    print(fi.evaluate(var_dict))
    print(fi.__str__())
    print(fi.getFreeVars())
    print(fi.tautology())
    fi2 = Or(Not(Variable("x")), Or(Variable("y"), Constant(True)))
    print(fi2.tautology())
    fi3 = Or(Not(Variable("x")), Or(Variable("y"), And(Variable("z"), Constant(False))))
    fi3 = fi3.simplify()
    print(fi3.__str__())

    fi3 * fi3


    fi = And(Variable("x"), And(Variable("y"), Constant(False)))
    print(fi.simplify())
    # var_dict2 = {"x": True, "y": 2}
    # fi.evaluate(var_dict2)