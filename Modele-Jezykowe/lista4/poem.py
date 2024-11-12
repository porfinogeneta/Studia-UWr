from transformers import AutoTokenizer, AutoModelWithLMHead, set_seed
model = AutoModelWithLMHead.from_pretrained('flax-community/papuGaPT2')
tokenizer = AutoTokenizer.from_pretrained('flax-community/papuGaPT2')
import torch
set_seed(42) # reproducibility

FILENAME = "poem.txt"

poem = """
Biega, krzyczy pan Hilary:
"Gdzie s¡ moje okulary"
Szuka w spodniach i w surducie,
W prawym bucie, w lewym bucie.
"""

with open(FILENAME, 'w', encoding="utf-8") as file:
    pass

input_ids = tokenizer.encode(poem, return_tensors='pt')


with open(FILENAME, "a", encoding="utf-8") as file:

    file.write("Poem Prompt Tokens:\n")
    poem_tokens = [tokenizer.decode(token_id) for token_id in input_ids[0]]
    for i, token in enumerate(poem_tokens):
        file.write(f"Token {i}: {token}\n")

    with torch.no_grad():
        outputs = model(input_ids)
        logits = outputs.logits

    last_token_logits = logits[0, -1, :]

    top_k_probs = torch.topk(last_token_logits, k=10)
    top_k_ids = top_k_probs.indices
    top_k_values = top_k_probs.values

    file.write("\nTop K Tokens from Last Token in Prompt:\n")
    for i, (token_id, prob) in enumerate(zip(top_k_ids, top_k_values)):
        top_k_token = tokenizer.decode([token_id])
        file.write(f"Top {i + 1}: {top_k_token}")
    

    output = model.generate(
        input_ids,
        do_sample=True, 
        max_new_tokens=50, 
        top_k=50, 
        top_p=0.95
    )[0]


    generated_text = tokenizer.decode(output, skip_special_tokens=True)
    file.write("\nGenerated Text:\n")
    file.write(generated_text)
