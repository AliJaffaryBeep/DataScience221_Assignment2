import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Data_science"

def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; DS221-Assignment/1.0)"
    }

    resp = requests.get(URL, headers=headers, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    # 1) Page title from <title>
    title_tag = soup.find("title")
    title_text = title_tag.get_text(strip=True) if title_tag else ""
    print(title_text)

     
    content = soup.find("div", id="mw-content-text")
    if not content:
        raise RuntimeError("Could not find div#mw-content-text")

    first_para = None
    for p in content.find_all("p"):
        text = p.get_text(" ", strip=True)
        if len(text) >= 50:
            first_para = text
            break

    if not first_para:
        raise RuntimeError("No paragraph with at least 50 characters found.")

    print(first_para)

if __name__ == "__main__":
    main()
