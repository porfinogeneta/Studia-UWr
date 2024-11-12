from categorizer import Categorizer
from heuristic import Heuristic
from llm_probability import LLMProbability
from polka import PolkaQuizSolver
from prompts import create_propmpt

if __name__ == "__main__":
    categorizer = Categorizer()
    cat_dict = categorizer.categorize_txt(filepath_questions="q&a/questions.txt", filepath_answers="q&a/answers.txt")
    
    # heurystyka dla pytań czy z opcjami wyboru
    heura = Heuristic()
    # print(heura.check_accuracy(cat_dict["czy_opt"]))

    # prawdopodobieństwo dla pytań czy z odpowiedzią tak/nie
    llm_prop = LLMProbability()
    # print(llm_prop.determine_answer("Czy rozgwiazdy są zwierzętami drapieżnymi?"))
    # print(llm_prop.check_accuracy(cat_dict["czy"]))


    polka = PolkaQuizSolver()

    # zero_q = ["Czy Uniwersytet Cambridge znajduje się w amerykańskim mieście o tej samej nazwie?", 
    #           "W której balladzie Adam Mickiewicz deklarował: „czucie i wiara silniej mówi do mnie niż mędrca szkiełko i oko”?",
    #           "Kto pomógł nieść krzyż Jezusowi w drodze na Golgotę?", "Ile wynosi pierwiastek trzeciego stopnia z ośmiu?",
    #           "Jak nazywają się boczne pasy na mundurowych spodniach?", "Czy waltornia to instrument dęty blaszany czy drewniany?"]

    # for q in zero_q:
    #     print("\n\n", polka.answer_question(question=q, prompt_type="one"), "\n===============")
    # print(polka.check_accuracy(categories_dict=cat_dict, prompt_type="zero", category="czy"))
    categories = ["czy", "czy_opt", "jak+", "ile", "w_ktorym+", "kto", "rest"]
    prompt_types = ["zero", "one", "few"]
    total = 0
    correct = 0
    with open('sample_res22.txt', 'w', encoding="utf-8") as file:
        for c in categories:
            for pt in ["few"]:
                accuracy, cor, tot = polka.check_accuracy(categories_dict=cat_dict,
                                                          prompt_type=pt,
                                                          category=c,
                                                          amount_from_category=10)
                total += tot
                correct += cor
                result_line = f"Category: {c:<20} Accuracy: {accuracy:.2%} Prompt-type: {pt} In category: {len(cat_dict[c])}"
                file.write(result_line + '\n')
        
        file.write('-' * 60 + '\n')

    #     overall_accuracy = correct / total if total > 0 else 0
    #     file.write(f"Overall accuracy: {overall_accuracy:.2%}\nTotal: {total}\nCorrect:{correct}")
   
    # with open("dict.txt", "w") as file:
    #     for key, values in cat_dict.items():
            
    #         for value in values[:5]:  # Slicing to get the first 5 items
    #             print(f"{key} - {len(cat_dict[key])} - {value}", file=file)
    #         print() 

