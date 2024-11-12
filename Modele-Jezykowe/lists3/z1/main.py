import random
from polka import PolkaCalculator
from prompts import create_rigid_propmt, create_few_shot_text_prompt, create_programatic_text_prompt


if __name__ == "__main__":

    CORRECT = 0
    POLKA = PolkaCalculator()

    # POLKA.determine_accuracy(prompt_type="addition", 
    #                         complexity="addition_few",
    #                         rg=(0,9),
    #                         operation="+",
    #                         total=20)

    # rigid prompts
    operations = ["+", "*", "-", "/"]
    operators_map = {
        "+": "addition",
        "-": "substraction",
        "*": "multiplication",
        "/": "division"
    }

    prt_type = ["_rigissd", "_few_shssots", "_prograssmmatic"]
    
    eq_n = 5
    rg = (1,10)
    # for op in operations:
    #     for pt in prt_type:
    #         POLKA.determine_accuracy(operation=op,
    #                                 operation_type=operators_map[op],
    #                                 complexity=f"{operators_map[op]}{pt}",
    #                                 rg=(1,10),
    #                                 prompt_generator=create_programatic_text_prompt,
    #                                 total=10)
        

    # PLOTTING RESULTS
    # files_rigid = ["results/addition/addition_rigid_1.txt", "results/division/division_rigid_1.txt", "results/multiplication/multiplication_rigid_1.txt", "results/substraction/substraction_rigid_1.txt"]
    # POLKA.extract_and_plot_multiple(file_paths=files_rigid, title="Rigid Prompts")

    # files_full_text = ["results/addition/addition_few_shots_1.txt", "results/division/division_few_shots_1.txt", "results/multiplication/multiplication_few_shots_1.txt", "results/substraction/substraction_few_shots_1.txt"]
    # POLKA.extract_and_plot_multiple(file_paths=files_full_text, title="Few Shots Prompts")

    # files_programmatic = ["results/addition/addition_programmatic_1.txt", "results/division/division_programmatic_1.txt", "results/multiplication/multiplication_programmatic_1.txt", "results/substraction/substraction_programmatic_1.txt"]
    # POLKA.extract_and_plot_multiple(file_paths=files_programmatic, title="Programmatic Prompts")

    files_dict = {
    "Rigid Prompts": ["results/addition/addition_rigid_1.txt",
                      "results/division/division_rigid_1.txt",
                      "results/multiplication/multiplication_rigid_1.txt",
                      "results/substraction/substraction_rigid_1.txt"],
                      
    "Few Shots Prompts": ["results/addition/addition_few_shots_1.txt",
                         "results/division/division_few_shots_1.txt",
                         "results/multiplication/multiplication_few_shots_1.txt",
                         "results/substraction/substraction_few_shots_1.txt"],
                         
    "Programmatic Prompts": ["results/addition/addition_programmatic_1.txt",
                            "results/division/division_programmatic_1.txt",
                            "results/multiplication/multiplication_programmatic_1.txt",
                            "results/substraction/substraction_programmatic_1.txt"]
}

POLKA.extract_and_plot_combined(files_dict)