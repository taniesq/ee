def evaluate_generation(corpus, output):
    def get_tokens(path):
        with open(path, "r") as f:
            return f.read().lower().split()

    corpus_tokens = get_tokens(corpus)
    output_tokens = get_tokens(output)

    corpus_vocab = set(corpus_tokens)
    output_vocab = set(output_tokens)

    # unigrams
    distinct_1 = len(output_vocab) / len(output_tokens)

    # a comparison to the corpus
    # AKA how many of the words from the corpus appeared in the output?
    coverage = len(output_vocab.intersection(corpus_vocab)) / len(corpus_vocab)

    # novelty
    # or, perhaps, how many 'original' words have been generated
    novel_words = len(output_vocab - corpus_vocab)

    return {
        "unigrams": round(distinct_1, 4),
        "corpus-based comparison": f"{round(coverage * 100, 2)}%",
        "novelty number": novel_words
    }

# pick one output file to de-comment & then run the code

# results = evaluate_generation("corpus.txt", "markoutput.txt")
# results = evaluate_generation("corpus.txt", "llm_out.txt")
print(results)