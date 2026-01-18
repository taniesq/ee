def calculate_distinct_n(file_path):

    with open("ffinal/markoutput.txt", "r") as f:
        tokens = f.read().lower().split()

    tokens_count = len(tokens)

    unigrams = tokens
    distinct_1 = len(set(unigrams)) / len(unigrams)

    bigrams = [f"{tokens[i]} {tokens[i + 1]}" for i in range(len(tokens) - 1)]
    
    if len(bigrams) > 0:
        distinct_2 = len(set(bigrams)) / len(bigrams)
    else:
        distinct_2 = 0

    print(f"total tokens = {tokens_count}")
    print(f"unigrams = {round(distinct_1, 4)}")
    print(f"bigrams = {round(distinct_2, 4)}")

results = calculate_distinct_n("ffinal/corpus.txt")
print(results)