import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
from typing import List
from probability_sentence import sentence_prob

# SET UP THE CHATBOT
# Set the device to MPS if available, otherwise use CPU
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

model_name = "eryk-mazus/polka-1.1b-chat"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,  # MPS doesn't support bfloat16
    device_map="auto"
)

# Move the model to the appropriate device
model.to(device)

streamer = TextStreamer(tokenizer, skip_prompt=True)

# You are a helpful assistant.
system_prompt = "Jesteś pomocnym asystentem. \
    Prowadzisz rozmowę z użytkownikiem na temat pogody. \
    Postaraj się aby twoje odpowiedzi były krótkie i treściwe!"
chat = [{"role": "system", "content": system_prompt}]


def generate_response(user_input: str):

    # Compose a short song on programming.
    chat.append({"role": "user", "content": user_input})

    # Generate - add_generation_prompt to make sure it continues as assistant
    inputs = tokenizer.apply_chat_template(chat, add_generation_prompt=True, return_tensors="pt")

    # Move inputs to the same device as the model
    inputs = inputs.to(device)

    possible_resps = []

    for _ in range(3):
        with torch.no_grad():
            outputs = model.generate(
                inputs,
                pad_token_id=tokenizer.eos_token_id,
                max_new_tokens=30,
                temperature=0.2,
                repetition_penalty=1.15,
                top_p=0.95,
                do_sample=True,
            )

        new_tokens = outputs[0, inputs.size(1):]
        response = tokenizer.decode(new_tokens, skip_special_tokens=True)

        # get rid of ending a response mid-sentence
        possible_resps.append(end_response(response=response))

    optimal_response = choose_optimal_response(possible_resps)

    chat.append({"role": "assistant", "content": optimal_response})
    
    return optimal_response

def end_response(response: str):
    response_trailed = response.rstrip()
    if not response_trailed.endswith(".") or not response_trailed.endswith("?") or response_trailed.endswith("!"):
        last_sentence = max(response.rfind("."), response.rfind("?"), response.rfind("!"))
        if last_sentence == -1:
            return response + "."
        else:
            return response[:last_sentence + 1]
        
    

def choose_optimal_response(responses: List[str]):
    mx_prob = float("-inf")
    mx_resp = ""
    for res in responses:
        prob = sentence_prob(res)
        if prob > mx_prob:
            mx_resp = res
            mx_prob = prob
    
    return mx_resp


if __name__ == "__main__":
    print("Chatbot initialized. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        response = generate_response(user_input=user_input)
        print(response)
    