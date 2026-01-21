def evaluate_generation(corpus, output):
    # load and tokenize both files
    with open(corpus, "r") as f:
        c_tokens = f.read().lower().split()
    with open(output, "r") as f:
        o_tokens = f.read().lower().split()

    # unigrams
    c_uni = set(c_tokens)
    o_uni = set(o_tokens)
    
    uni_distinct = len(o_uni) / len(o_tokens) 
    # how many words from the corpus appeared in the output:
    uni_coverage = len(o_uni.intersection(c_uni)) / len(c_uni)
    # how many original words have been generated:
    uni_novelty = len(o_uni - c_uni)

    # bigrams
    c_bi = set(f"{c_tokens[i]} {c_tokens[i+1]}" for i in range(len(c_tokens)-1))
    o_bi = set(f"{o_tokens[i]} {o_tokens[i+1]}" for i in range(len(o_tokens)-1))
    
    bi_total = len(o_tokens) - 1
    bi_distinct = len(o_bi) / bi_total 
    bi_coverage = len(o_bi.intersection(c_bi)) / len(c_bi) 
    bi_novelty = len(o_bi - c_bi)

    # trigrams
    c_tri = set(f"{c_tokens[i]} {c_tokens[i+1]} {c_tokens[i+2]}" for i in range(len(c_tokens)-2))
    o_tri = set(f"{o_tokens[i]} {o_tokens[i+1]} {o_tokens[i+2]}" for i in range(len(o_tokens)-2))
    
    tri_total = len(o_tokens) - 2
    tri_distinct = len(o_tri) / tri_total
    tri_coverage = len(o_tri.intersection(c_tri)) / len(c_tri)
    tri_novelty = len(o_tri - c_tri)

    return {
        "unigrams": round(uni_distinct, 4),
        "unigram coverage": f"{round(uni_coverage * 100, 2)}%",
        "unigram novelty": uni_novelty,
        
        "bigrams": round(bi_distinct, 4),
        "bigram coverage": f"{round(bi_coverage * 100, 2)}%",
        "bigram novelty": bi_novelty,
        
        "trigrams": round(tri_distinct, 4),
        "trigram coverage": f"{round(tri_coverage * 100, 2)}%",
        "trigram novelty": tri_novelty
    }

# pick one output file to de-comment & then run the code

# results = evaluate_generation("corpus.txt", "markoutput.txt")
# results = evaluate_generation("corpus.txt", "llm_out.txt")

print(results)