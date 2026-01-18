# Data Setup
nouns = [
    "apple", "pear", "orange", "house", "farm", "cow", "goat", "sheep", 
    "chicken", "hen", "pig", "human", "star", "planet", "robot", "pea", 
    "book", "shoe", "sock", "hook", "needle", "yarn", "sunhat", "car", "doll"
]

# Modals to be added to the base form of verbs 1-21
modals = ["should", "must", "has to", "cannot", "can"]

# Verbs 1-21 (with prepositions where needed)
v_data = [
    ("eat", ""), ("jump", "over"), ("drink", ""), ("drown", "in"),
    ("swim", "across"), ("dance", "with"), ("throw", ""), ("paint", ""),
    ("draw", ""), ("squeeze", ""), ("create", ""), ("speak", "to"),
    ("play", "with"), ("hold", ""), ("craft", ""), ("dress", ""),
    ("twirl", "around"), ("orbit", ""), ("multiply", ""), ("admire", ""),
    ("pull", ""), ("write", "")
]

all_verb_variants = []

# Generate variants for first 21 verbs
for base, prep in v_data:
    # 1-5: Modal + Base
    for m in modals:
        all_verb_variants.append({"v": f"{m} {base}", "p": prep})
    
    # 6: Singular (eats, jumps, etc.)
    if base.endswith('y') and base != "play": # basic suffix logic for "multiplies"
        sing = base[:-1] + "ies"
    elif base.endswith(('sh', 'ss', 'ch')):
        sing = base + "es"
    else:
        sing = base + "s"
    all_verb_variants.append({"v": sing, "p": prep})

    # 7: Past (ate, jumped, etc.) - Manual override for irregulars if desired, 
    # but using your provided logic:
    past_map = {"eat":"ate", "jump":"jumped", "drink":"drank", "drown":"drowned", 
                "swim":"swam", "dance":"danced", "throw":"threw", "paint":"painted",
                "draw":"drew", "squeeze":"squeezed", "create":"created", "speak":"spoke",
                "play":"played", "hold":"held", "craft":"crafted", "dress":"dressed",
                "twirl":"twirled", "orbit":"orbited", "multiply":"multiplied", 
                "admire":"admired", "pull":"pulled", "write":"wrote"}
    all_verb_variants.append({"v": past_map[base], "p": prep})

    # 8: Future
    all_verb_variants.append({"v": f"will {base}", "p": prep})

    # 9: Perfect
    perf_map = {"eat":"has eaten", "jump":"has jumped", "drink":"has drank", "drown":"has drowned", 
                "swim":"has swum", "dance":"has danced", "throw":"has thrown", "paint":"has painted",
                "draw":"has drawn", "squeeze":"has squeezed", "create":"has created", "speak":"has spoken",
                "play":"has played", "hold":"has held", "craft":"has crafted", "dress":"has dressed",
                "twirl":"has twirled", "orbit":"has orbited", "multiply":"has multiplied", 
                "admire":"has admired", "pull":"has pulled", "write":"has written"}
    all_verb_variants.append({"v": perf_map[base], "p": prep})

# Setup Noun Pairs (S != O)
noun_pairs = [(s, o) for s in nouns for o in nouns if s != o]

articles = ["a", "the", "this", "that"]
lines = []

for i in range(5000):
    sub, obj = noun_pairs[i % len(noun_pairs)]
    verb_info = all_verb_variants[i % len(all_verb_variants)]
    
    art1 = articles[(i // 10) % len(articles)]
    art2 = articles[i % len(articles)]
    
    v_str = verb_info["v"]
    prep = verb_info["p"]
    
    if prep:
        sentence = f"{art1} {sub} {v_str} {prep} {art2} {obj}"
    else:
        sentence = f"{art1} {sub} {v_str} {art2} {obj}"
    
    lines.append(sentence)

with open("final_grammatically_correct.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")

print("out done!")