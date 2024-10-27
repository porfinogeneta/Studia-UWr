from determine_if_common import DetermineIfCommon
from txt_prob import sentence_prob
    
sentences = [
  'To jest zwykłe polskie zdanie.',
  'This is a normal English sentence.',
  'iweryuiiu hrfw3eieur fr',
  "Wczoraj wieczorem spotkałem pewną wspaniałą kobietę, która z pasją opowiadała o modelach językowych."
]
    
    
if __name__ == "__main__":
    check_common = DetermineIfCommon()
    # check_common.find_the_most_natural_sentences(sentence='To jest zwykłe polskie zdanie.', filename="smaple_short.txt")
    check_common.find_the_most_natural_sentences(
                                        sentence='Wczoraj wieczorem spotkałem pewną wspaniałą kobietę, która z pasją opowiadała o modelach językowych.',
                                        filename="polskie_zdanie_fixed?.txt"
                                        )