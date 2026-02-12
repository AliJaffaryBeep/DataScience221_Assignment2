import csv
import requests
from bs4 import BeautifulSoup
from pathlib import Path

URL = "https://en.wikipedia.org/wiki/Machine_learning"

def clean_cell(cell) -> str:
  
    return " ".join(cell.get_text(" ", strip=True).split())

def main():
    headers = {"User-Agent": "Mozilla/5.0 (compatible; DS221-Assignment/1.0)"}
    resp = requests.get(URL, headers=headers, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    content = soup.find("div", id="mw-content-text")
    if not content:
        raise RuntimeError("Could not find div#mw-content-text")

    target_table = None
    target_rows = None


    for table in content.find_all("table"):
        rows = table.find_all("tr")
        data_rows = []
        for tr in rows:
            tds = tr.find_all("td")
            if tds:
                data_rows.append(tr)

        if len(data_rows) >= 3:
            target_table = table
            target_rows = rows
            break

    if target_table is None:
        raise RuntimeError("No table with at least 3 data rows found.")


    header = []
    header_row = None
    for tr in target_table.find_all("tr"):
        ths = tr.find_all("th")
        if ths:
            header_row = tr
            header = [clean_cell(th) for th in ths]
            break


    data = []
    max_cols = 0
    for tr in target_table.find_all("tr"):
        tds = tr.find_all("td")
        if not tds:
            continue
        row = [clean_cell(td) for td in tds]
        data.append(row)
        max_cols = max(max_cols, len(row))


    if not header:
        header = [f"col{i}" for i in range(1, max_cols + 1)]
    else:

        if len(header) < max_cols:
            header += [f"col{i}" for i in range(len(header) + 1, max_cols + 1)]
        elif len(header) > max_cols:
            max_cols = len(header)


    for row in data:
        if len(row) < max_cols:
            row += [""] * (max_cols - len(row))

    out_path = Path(__file__).resolve().parent / "wiki_table.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

    print(f"Saved table with {len(data)} rows and {len(header)} columns to: {out_path}")

if __name__ == "__main__":
    main()
