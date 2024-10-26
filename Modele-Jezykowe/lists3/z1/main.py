import random
from polka import PolkaCalculator

if __name__ == "__main__":

    CORRECT = 0
    POLKA = PolkaCalculator()

    # POLKA.determine_accuracy(prompt_type="addition", 
    #                         complexity="addition_one_digit",
    #                         rg=(0,9),
    #                         operation="+",
    #                         total=20)
    # POLKA.determine_accuracy(prompt_type="addition",
    #                         complexity="addition_two_digits", 
    #                         rg=(10,99), 
    #                         operation=lambda x,y: x+y,
    #                         total=20)

    # POLKA.determine_accuracy(prompt_type="multiplication", 
    #                         complexity="multiplication_one_digit",
    #                         rg=(0,9),
    #                         operation="*",
    #                         total=10)
    
    POLKA.determine_accuracy(prompt_type="division", 
                            complexity="division_one_digit",
                            rg=(1,9),
                            operation="/",
                            total=10)


