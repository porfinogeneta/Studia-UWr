import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from torch.nn import functional as F
from typing import List
from tqdm import tqdm


model_name = 'flax-community/papuGaPT2'
device = 'cuda'
device = 'cpu'

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

def log_probs_from_logits(logits, labels):
    logp = F.log_softmax(logits, dim=-1)
    logp_label = torch.gather(logp, 2, labels.unsqueeze(2)).squeeze(-1)
    return logp_label
    
            
def sentence_prob(sentence_txt):
    input_ids = tokenizer(sentence_txt, return_tensors='pt')['input_ids'].to(device)
    with torch.no_grad():
        output = model(input_ids=input_ids)
        log_probs = log_probs_from_logits(output.logits[:, :-1, :], input_ids[:, 1:])
        seq_log_probs = torch.sum(log_probs)
    return seq_log_probs.cpu().numpy()  
    
# sentences = [
#   'To jest zwykłe polskie zdanie.',
#   'This is a normal English sentence.',
#   'iweryuiiu hrfw3eieur fr',
# ]

# print ()
# for s in sentences:
#     print (s, sentence_prob(s))

# LLM będzie obliczał ppb odpowiedzi tak/nie w pytanich czy
class LLMProbability:

    def __init__(self) -> None:
        self.yes = "To jest neutralne zdanie: tak"
        self.no = "To jest neutralne zdanie: nie"

    def normalize(self):
        yes_p = sentence_prob(self.yes)
        no_p = sentence_prob(self.no)
        return abs(yes_p - no_p)
    
    def determine_answer(self, question: str) -> str:

        normalize_factor = self.normalize()

        # print("normalize factor", normalize_factor)

        # przeskalowujemy odpowiedzi, bo model jest zbiasowany delikatnie na 'nie'
        p_yes_sen = sentence_prob(f"{question} {self.yes}") + normalize_factor
        p_no_sen = sentence_prob(f"{question} {self.yes}")

        return "tak" if p_yes_sen > p_no_sen else "nie"
    
    # q_ato lista złożona z [question, [answer1, answer2]]
    def check_accuracy(self, q_a: List[List]) -> float:
        czy_answers =[p[1][0] for p in q_a] # weź tak/nie z odpowiedzi
        czy_questions = [p[0] for p in q_a]

        total = len(q_a)
        correct = 0

        for i in tqdm(range(total)):
            more_probable = self.determine_answer(czy_questions[i])
            # czy dobrze obliczyliśmy na podstawie ppb modelu
            if czy_answers[i] == more_probable:
                correct += 1

        return correct / total
                



    
