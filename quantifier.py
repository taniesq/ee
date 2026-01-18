def evaluate_generation(corpus, output):
    def get_tokens(path):
        with open(path, "r") as f:
            return f.read().lower().split()
        
    def get_bigrams(tokens):
        return [f"{tokens[i]} {tokens[i+1]}" for i in range(len(tokens)-1)]
    
    corpus_tokens = get_tokens(corpus)
    output_tokens = get_tokens(output)

    corpus_vocab = set(corpus_tokens)
    output_vocab = set(output_tokens)
    
    corpus_bigram_set = set(get_bigrams(corpus_tokens))
    output_bigram_set = set(get_bigrams(output_tokens))

    # unigrams
    distinct_1 = len(output_vocab) / len(output_tokens)
    uni_coverage = len(output_vocab.intersection(corpus_vocab)) / len(corpus_vocab)
    uni_novelty = len(output_vocab - corpus_vocab)

    # bigrams
    distinct_2 = len(output_bigram_set) / (len(output_tokens) - 1) if len(output_tokens) > 1 else 0

    # a comparison to the corpus
    # AKA how many of the words from the corpus appeared in the output?
    bi_coverage = len(output_bigram_set.intersection(corpus_bigram_set)) / len(corpus_bigram_set)

    # novelty
    # or, perhaps, how many 'original' words have been generated
    novel_bigrams = len(output_bigram_set - corpus_bigram_set)

    return {
        "unigrams": round(distinct_1, 4),
        "unigram coverage": f"{round(uni_coverage * 100, 2)}%",
        "unigram novelty": uni_novelty,
        "bigrams": round(distinct_2, 4),
        "bigram coverage": f"{round(bi_coverage * 100, 2)}%",
        "bigram novelty": novel_bigrams
    }

# pick one output file to de-comment & then run the code

# results = evaluate_generation("corpus.txt", "markoutput.txt")
# results = evaluate_generation("corpus.txt", "llm_out.txt")
print(results)