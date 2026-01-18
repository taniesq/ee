import markovify
import random

random.seed(64) # for reproducibility

with open("/Users/tazzie/Desktop/m26ee/ffinal/corpus.txt", "r") as corpus:
   text = corpus.read(); 

print(len(text))

model = markovify.NewlineText(text, state_size = 3)

def generate_lines(n = 100, max_chars = 120):
    output = set()

    while len(output) < n:
        line = None
        tries = 0

        while line is None and tries < 50:
            line = model.make_short_sentence(char_limit = max_chars, tries = 20)
            tries = tries + 1
    
        if line is not None:
            output.add(line)

    return list(output)

markoutput = generate_lines(100)

for line in markoutput:
    print(line)

with open("/Users/tazzie/Desktop/m26ee/ffinal/markoutput.txt", "w") as file:
    for line in markoutput:
        file.write(line + "\n")