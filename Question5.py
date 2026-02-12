import pandas as pd
from pathlib import Path

def main():
    base = Path(__file__).resolve().parent
    in_file = base / "Data" / "student.csv"
    out_file = base / "Data" / "student_bands.csv"

    df = pd.read_csv(in_file, sep=None, engine="python")


    df["grade"] = pd.to_numeric(df["grade"], errors="coerce")
    df["absences"] = pd.to_numeric(df["absences"], errors="coerce")
    df["internet"] = pd.to_numeric(df["internet"], errors="coerce")


    df["grade_band"] = pd.cut(
        df["grade"],
        bins=[-float("inf"), 9, 14, float("inf")],
        labels=["Low", "Medium", "High"],
        right=True,
        include_lowest=True,
    )

    summary = (
        df.groupby("grade_band", dropna=False)
          .agg(
              num_students=("grade", "size"),
              avg_absences=("absences", "mean"),
              pct_internet=("internet", lambda s: s.mean() * 100),
          )
          .reset_index()
    )

    summary.to_csv(out_file, index=False)

    print(summary)

if __name__ == "__main__":
    main()
