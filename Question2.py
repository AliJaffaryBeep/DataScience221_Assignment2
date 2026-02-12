from collections import Counter
import string

PUNCT = string.punctuation

def cleaned_tokens(filename: str):
    tokens = []
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            for raw in line.split():
                token = raw.lower().strip(PUNCT)


                if sum(ch.isalpha() for ch in token) >= 2:
                    tokens.append(token)
    return tokens

def top_5_bigrams(filename: str) -> None:
    tokens = cleaned_tokens(filename)

    bigram_counts = Counter()
    for i in range(len(tokens) - 1):
        bigram = (tokens[i], tokens[i + 1])
        bigram_counts[bigram] += 1


    top5 = sorted(bigram_counts.items(), key=lambda x: (-x[1], x[0]))[:5]

    for (w1, w2), count in top5:
        print(f"{w1} {w2} -> {count}")

if __name__ == "__main__":
    top_5_bigrams("/Data/sample-file.txt")
