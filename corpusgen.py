# all nouns
nouns = [
    "apple", "pear", "orange", "house", "farm", "cow", "goat", "sheep", 
    "chicken", "hen", "pig", "human", "star", "planet", "robot", "pea", 
    "book", "shoe", "sock", "hook", "needle", "yarn", "sunhat", "car", "doll"
]

# adding modal verbs
modals = ["should", "must", "has to", "cannot", "can"]

# all verbs
verbs = [
    ("eat", ""), ("jump", "over"), ("drink", ""), ("drown", "in"),
    ("swim", "across"), ("dance", "with"), ("throw", ""), ("paint", ""),
    ("draw", ""), ("squeeze", ""), ("create", ""), ("speak", "to"),
    ("play", "with"), ("hold", ""), ("craft", ""), ("dress", ""),
    ("twirl", "around"), ("orbit", ""), ("multiply", ""), ("admire", ""),
    ("pull", ""), ("write", "")
]

all_verb_vars = []

for base, prep in verbs:
    for m in modals:
        all_verb_vars.append({"v": f"{m} {base}", "p": prep})
    
    # singular verbs that need modals added to them
    if base.endswith('y') and base != "play":
        sing = base[:-1] + "ies"
    elif base.endswith(('sh', 'ss', 'ch')):
        sing = base + "es"
    else:
        sing = base + "s"
    all_verb_vars.append({"v": sing, "p": prep})

    past_map = {"eat":"ate", "jump":"jumped", "drink":"drank", "drown":"drowned", 
                "swim":"swam", "dance":"danced", "throw":"threw", "paint":"painted",
                "draw":"drew", "squeeze":"squeezed", "create":"created", "speak":"spoke",
                "play":"played", "hold":"held", "craft":"crafted", "dress":"dressed",
                "twirl":"twirled", "orbit":"orbited", "multiply":"multiplied", 
                "admire":"admired", "pull":"pulled", "write":"wrote"}
    all_verb_vars.append({"v": past_map[base], "p": prep})

    all_verb_vars.append({"v": f"will {base}", "p": prep})

    perf_map = {"eat":"has eaten", "jump":"has jumped", "drink":"has drank", "drown":"has drowned", 
                "swim":"has swum", "dance":"has danced", "throw":"has thrown", "paint":"has painted",
                "draw":"has drawn", "squeeze":"has squeezed", "create":"has created", "speak":"has spoken",
                "play":"has played", "hold":"has held", "craft":"has crafted", "dress":"has dressed",
                "twirl":"has twirled", "orbit":"has orbited", "multiply":"has multiplied", 
                "admire":"has admired", "pull":"has pulled", "write":"has written"}
    all_verb_vars.append({"v": perf_map[base], "p": prep})

# setting up the noun pairs
noun_pairs = [(s, o) for s in nouns for o in nouns if s != o]

articles = ["a", "the", "this", "that"]
lines = []

for i in range(5000):
    sub, obj = noun_pairs[i % len(noun_pairs)]
    verb_info = all_verb_vars[i % len(all_verb_vars)]
    
    art1 = articles[(i // 10) % len(articles)]
    art2 = articles[i % len(articles)]
    
    v_str = verb_info["v"]
    prep = verb_info["p"]
    
    if prep:
        sentence = f"{art1} {sub} {v_str} {prep} {art2} {obj}"
    else:
        sentence = f"{art1} {sub} {v_str} {art2} {obj}"
    
    lines.append(sentence)

with open("corpus.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")

print("corpus generated!")