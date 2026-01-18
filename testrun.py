import random

subjects_objects = [
    "apple", "pear", "house", "she", "he", "cow", "goat", "sheep",
    "orange", "teacher", "it", "backpack", "pillow", "headphones",
    "hat", "plate", "light", "human", "car"
]

verbs = [
    "accept", "admire", "announce", "burp", "prohibit",
    "bargain", "have", "rattle", "throw", "wear",
    "eat", "orbit", "personify", "bully", "act",
    "agree", "rain", "turn on", "turn off", "turn around"
]

prepositions = ["at", "to", "with", "around", "on"]
determiners = ["the", "a", "this", "that"]

random.seed(64)

sentences = []
used_triples = set()
used_mirrors = set()

while len(sentences) < 2500:
    subj = random.choice(subjects_objects)
    obj = random.choice(subjects_objects)
    verb = random.choice(verbs)
    prep = random.choice(prepositions)

    triple = (subj, verb, obj)
    mirror = (obj, verb, subj)

    if triple in used_triples:
        continue
    if mirror in used_triples and mirror not in used_mirrors:
        continue

    det_s = random.choice(determiners)
    det_o = random.choice(determiners)

    sentence = f"{det_s} {subj} {verb} {prep} {det_o} {obj}"

    sentences.append(sentence)
    used_triples.add(triple)
    used_mirrors.add(mirror)

output_path = "/Users/tazzie/Desktop/m26ee/ffinal/corpus.txt"
with open(output_path, "w") as f:
    for s in sentences:
        f.write(s + "\n")
