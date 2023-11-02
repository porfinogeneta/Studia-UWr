from collections import deque

# infiksowe ['(', 2, '+', 3, ')', '*', 4]
def convert(infix):
    # określenie pierwszeństwa
    def priority(t):
        if t in "+-":
            return 1
        elif t in "*/":
            return 2
        else:
            return 0

    output_queue = deque()
    operator_queue = deque()

    for token in infix:
        # liczba natychmiast dodana do output'u
        if isinstance(token, int):
            output_queue.append(token)
        # wyrażenie z nawiasem, rozpoczyna największy priotytet
        # dequeue append, dodaje na tył
        elif token == "(":
            operator_queue.append(token)
        elif token == ")":
            # dodajemy nasze operatory, dopóki nie dojdziemy do początku naszego nawiasu
            while operator_queue and operator_queue[-1] != "(":
                output_queue.append(operator_queue.pop())
            if operator_queue and operator_queue[-1] == "(":
                operator_queue.pop()
        else:
            # dodajemy operatory, sprawdzając je przy okazji ze stosem
            while operator_queue and priority(operator_queue[-1]) >= priority(token):
                output_queue.append(operator_queue.pop())
            operator_queue.append(token)

    # dodanie tego co ewentualnie zostało w kolejnce
    while operator_queue:
        output_queue.append(operator_queue.pop())

    return output_queue

# [2, 3, '+', 4, '*']
def count(rpn):
    # kolejka z liczbami
    nums = deque()
    operators = {"+", "-", "/", "*"}

    for token in rpn:
        if token not in operators:
            nums.append(token)
        else:
            num1 = nums.pop()
            num2 = nums.pop()

            result = 0
            # można użyć lambdy zamiast robić if'y
            if token == "*":
                result = num2 * num1
            elif token == "/":
                # dzielenie przez 0
                if num1 == 0:
                    return 0
                result = num2 / num1
            elif token == "-":
                result = num2 - num1
            elif token == "+":
                result = num2 + num1
            nums.append(result)
    return nums[0]

if __name__ == '__main__':
    print(convert(['(', 2, '+', 3, ')', '*', 4]))
    print(count(convert(['(', 2, '+', 3, ')', '/', 4])))