from transformers import AutoTokenizer, AutoModelWithLMHead, set_seed
model = AutoModelWithLMHead.from_pretrained('flax-community/papuGaPT2')
tokenizer = AutoTokenizer.from_pretrained('flax-community/papuGaPT2')
import torch
set_seed(42) # reproducibility

FILENAME = "res.txt"

prefixes = [
    "Wczoraj wieczorem postanowiłem",
    "Jeśli tylko miałbym więcej czasu",
    "Na świecie jest wiele miejsc, które",
    "Kiedy byłem dzieckiem, zawsze marzyłem o tym, żeby",
    "Jednym z największych wyzwań w życiu jest",
    "Najlepszy sposób na radzenie sobie z stresem to",
    "W przyszłości chciałbym zobaczyć",
    "Kiedy myślę o szczęściu, przychodzi mi na myśl",
    "Moim ulubionym wspomnieniem z wakacji jest",
    "Sztuka i kultura mają ogromne znaczenie, ponieważ",
    "Gdybym mógł podróżować w czasie, odwiedziłbym",
    "Ważne jest, aby pamiętać, że",
    "Czasami, aby osiągnąć sukces, trzeba",
    "Ludzie często zapominają, że",
    "Zaskoczyło mnie, kiedy dowiedziałem się, że"
]

with open(FILENAME, 'w') as file:
    pass

for p in prefixes:
    with open(FILENAME, "a") as file:
        print("Input:\n", p, "\n", 100 * '-', file=file)
        for i in range(2):
            if i % 2 == 1: 
                p += " "

            
            input_ids = tokenizer.encode(p, return_tensors='pt')

        
            with torch.no_grad():
                outputs = model(input_ids)
                logits = outputs.logits

            last_token_logits = logits[0, -1, :]

            top_k_probs = torch.topk(last_token_logits, k=10)
            top_k_ids = top_k_probs.indices
            top_k_values = top_k_probs.values

            top_k_tokens = [tokenizer.decode([token_id]) for token_id in top_k_ids]
            print(top_k_tokens, file=file)

            output = model.generate(
                input_ids,
                do_sample=False, 
                max_new_tokens=50, 
                top_k=50, 
                top_p=0.95
            )[0]


            print("Output:", "space" if i % 2 == 1 else "no space", 100 * '-', file=file)
            res = tokenizer.decode(output, skip_special_tokens=True)
            print(res, file=file)
            print(file=file)
        
        print(file=file)
    