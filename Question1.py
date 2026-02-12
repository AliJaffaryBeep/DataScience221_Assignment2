from collections import Counter
import string

PUNCT = string.punctuation

def top_10_words(filename: str) -> None:
    counts = Counter()

    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            for raw in line.split():
                token = raw.lower().strip(PUNCT)


                if sum(ch.isalpha() for ch in token) >= 2:
                    counts[token] += 1


    top10 = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:10]

    for word, count in top10:
        print(f"{word} -> {count}")

if __name__ == "__main__":
    top_10_words("data/sample-file.txt")