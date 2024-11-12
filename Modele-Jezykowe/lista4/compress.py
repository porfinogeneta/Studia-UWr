from transformers import AutoTokenizer, AutoModelWithLMHead, set_seed
model = AutoModelWithLMHead.from_pretrained('flax-community/papuGaPT2')
tokenizer = AutoTokenizer.from_pretrained('flax-community/papuGaPT2')
set_seed(42) # reproducibility
data = """Silnik parowy to jeden z kluczowych wynalazków, który zrewolucjonizował przemysł i transport w XVIII i XIX wieku. Jego działanie opiera się na wykorzystaniu energii cieplnej pary wodnej do napędu mechanizmów. Historia silnika parowego zaczyna się od pracy szkockiego wynalazcy Jamesa Watta, który w 1769 roku opracował bardziej wydajną wersję wcześniejszych modeli.

Silnik parowy działa na zasadzie zamiany energii cieplnej w energię mechaniczną. Woda jest podgrzewana w kotle, a powstała para wodna jest kierowana do cylindra, gdzie wypycha tłok. Ruch tłoka jest następnie przekształcany w ruch obrotowy, który może napędzać maszyny, lokomotywy czy statki.

Wprowadzenie silników parowych miało ogromny wpływ na rozwój przemysłu. Umożliwiło to produkcję na większą skalę oraz zrewolucjonizowało transport, wprowadzając lokomotywy parowe na tory i statki parowe na wody. Silnik parowy przyczynił się również do urbanizacji, gdyż ułatwił przewóz towarów i ludzi do miast.

Pomimo że silniki parowe zostały stopniowo zastąpione przez silniki spalinowe i elektryczne, ich wpływ na rozwój technologii i gospodarki pozostaje niezatarte. Do dziś są symbolem epoki przemysłowej i innowacji, a także ważnym elementem historii technologii. Współczesne zastosowania silników parowych można znaleźć w niektórych dziedzinach, takich jak energetyka, gdzie parowe turbiny generują elektryczność w elektrowniach."""

sen = """Silnik parowy to jeden z kluczowych wynalazków, który zrewolucjonizował przemysł i transport w XVIII i XIX wieku. Jego działanie opiera się na wykorzystaniu energii cieplnej pary wodnej do napędu mechanizmów. Historia silnika parowego zaczyna się od pracy szkockiego wynalazcy Jamesa Watta, który w 1769 roku opracował bardziej wydajną wersję wcześniejszych modeli."""

input_ids = tokenizer.encode(sen, return_tensors='pt')

sample_outputs = model.generate(
    input_ids,
    do_sample=False, 
    max_new_tokens=10, 
    top_k=0, 
    top_p=1.0, 
    temperature=1.0
)

print("Output:\
" + 100 * '-')
for i, sample_output in enumerate(sample_outputs):
  print("{}: {}".format(i, tokenizer.decode(sample_output, skip_special_tokens=True)))
  