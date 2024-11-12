from polka_generator import PolkaGenerator
import random

FILENAME = "prefiksy.txt"

def sample_text_lines(num_samples=3, seed=None):
    if seed is not None:
        random.seed(seed)
    
    try:
        with open(FILENAME, 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]
        
        num_samples = min(num_samples, len(lines))
        
        samples = random.sample(lines, num_samples)
        
        return samples
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find file: {FILENAME}")
   

if __name__ == "__main__":
    # prompt = "Warto wypróbować więc"
    polka = PolkaGenerator()
    # polka.generate(prompt=prompt, letter="p")
    # polka.variants_generation(quantity=5, prefix=prompt)
    # polka.find_best_variant(5, prompt)
    prompts = sample_text_lines(10)
    print(prompts)
    with open('smaller_sample.txt', 'w') as file:
        for p in prompts:
            print(f"{p}\n{polka.find_best_variant(variants_quantity=5, prefix=p)}\n", file=file)