import pandas as pd
from pathlib import Path

def main():
    base = Path(__file__).resolve().parent
    in_file = base / "Data" / "student.csv"
    out_file = base / "Data" / "high_engagement.csv"

    print("Reading:", in_file)
    print("Exists:", in_file.exists())

    df = pd.read_csv(in_file, sep=None, engine="python")
    print("Loaded rows:", len(df))
    print("Columns:", list(df.columns))

    filtered = df[(df["studytime"] >= 3) & (df["internet"] == 1) & (df["absences"] <= 5)]
    filtered.to_csv(out_file, index=False)

    num_students = len(filtered)
    avg_grade = pd.to_numeric(filtered["grade"], errors="coerce").mean()

    print("Saved:", out_file)
    print(num_students)
    print(avg_grade)

if __name__ == "__main__":
    main()
