import pandas as pd
from pathlib import Path

def main():
    base = Path(__file__).resolve().parent
    in_file = base / "Data" / "crime.csv"

    df = pd.read_csv(in_file, sep=None, engine="python")

    df["ViolentCrimesPerPop"] = pd.to_numeric(df["ViolentCrimesPerPop"], errors="coerce")
    df["PctUnemployed"] = pd.to_numeric(df["PctUnemployed"], errors="coerce")

    df["risk"] = df["ViolentCrimesPerPop"].apply(lambda x: "HighCrime" if x >= 0.50 else "LowCrime")

    avgs = df.groupby("risk")["PctUnemployed"].mean()

    high = avgs.get("HighCrime", float("nan"))
    low = avgs.get("LowCrime", float("nan"))

    print(f"HighCrime avg PctUnemployed: {high}")
    print(f"LowCrime avg PctUnemployed: {low}")

if __name__ == "__main__":
    main()
