import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from torch.nn import functional as F
import random

model_name = 'flax-community/papuGaPT2'
device = 'cuda'
device = 'cpu'

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

class SentenceProabability():
    
    def __init__(self) -> None:
        pass


    def __log_probs_from_logits(self, logits, labels):
        logp = F.log_softmax(logits, dim=-1)
        logp_label = torch.gather(logp, 2, labels.unsqueeze(2)).squeeze(-1)
        return logp_label
    
    def sentence_prob(self, sentence_txt):
        input_ids = tokenizer(sentence_txt, return_tensors='pt')['input_ids'].to(device)
        with torch.no_grad():
            output = model(input_ids=input_ids)
            log_probs = self.__log_probs_from_logits(output.logits[:, :-1, :], input_ids[:, 1:])
            seq_log_probs = torch.sum(log_probs)
        return seq_log_probs.cpu().numpy()  
    

    
