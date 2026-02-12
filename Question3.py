from collections import defaultdict

def normalize_line(s: str) -> str:

    return "".join(ch for ch in s.lower() if ch.isalnum())

def find_near_duplicate_sets(filename: str) -> None:
    groups = defaultdict(list)

    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for line_num, line in enumerate(f, start=1):
            original = line.rstrip("\n")
            key = normalize_line(original)
            groups[key].append((line_num, original))


    dup_sets = [items for items in groups.values() if len(items) >= 2]

    print(len(dup_sets))


    for set_idx, items in enumerate(dup_sets[:2], start=1):
        print(f"\nSet {set_idx}:")
        for line_num, original in items:
            print(f"{line_num}: {original}")

if __name__ == "__main__":
    find_near_duplicate_sets("data/sample-file.txt")


