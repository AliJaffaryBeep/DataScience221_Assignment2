from pathlib import Path

def find_lines_containing(filename, keyword):
    """
    Returns a list of (line_number, line_text) for lines that contain the keyword
    (case-insensitive). Line numbers start at 1.
    """
    results = []
    key = keyword.lower()

    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for line_num, line in enumerate(f, start=1):
            if key in line.lower():
                results.append((line_num, line.rstrip("\n")))

    return results

def main():
    base = Path(__file__).resolve().parent
    file_path = base / "Data" / "sample-file.txt"

    matches = find_lines_containing(file_path, "lorem")

    print(f"Number of matching lines: {len(matches)}")
    print("First 3 matching lines:")

    for line_num, text in matches[:3]:
        print(f"{line_num}: {text}")

if __name__ == "__main__":
    main()
