import requests
from bs4 import BeautifulSoup
from pathlib import Path

URL = "https://en.wikipedia.org/wiki/Data_science"
BANNED_WORDS = ["references", "external links", "see also", "notes"]

def clean_heading_text(h2_tag) -> str:
    span = h2_tag.find("span", class_="mw-headline")
    text = span.get_text(" ", strip=True) if span else h2_tag.get_text(" ", strip=True)
    text = text.replace("[edit]", "").strip()
    return " ".join(text.split())

def main():
    headers = {"User-Agent": "Mozilla/5.0 (compatible; DS221-Assignment/1.0)"}
    resp = requests.get(URL, headers=headers, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    content = soup.find("div", id="mw-content-text")
    if not content:
        raise RuntimeError("Could not find div#mw-content-text")

    headings = []
    for h2 in content.find_all("h2"):
        text = clean_heading_text(h2)
        if not text:
            continue

        low = text.lower()
        if any(bad in low for bad in BANNED_WORDS):
            continue

        headings.append(text)

    out_path = Path(__file__).resolve().parent / "headings.txt"
    out_path.write_text("\n".join(headings) + "\n", encoding="utf-8")

    print(f"Saved {len(headings)} headings to: {out_path}")

if __name__ == "__main__":
    main()
