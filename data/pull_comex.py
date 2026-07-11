"""Pull Brazilian iron ore exports (HS4 2601) from Comex Stat bulk files.

Downloads yearly EXP files from the official open-data endpoint,
filters to iron ore, aggregates to monthly tonnes.
"""
from pathlib import Path
import pandas as pd

BASE_URL = "https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_{year}.csv"
RAW_DIR = Path(__file__).parent / "raw" / "comexstat"
OUT_PATH = Path(__file__).parent / "processed" / "iron_ore_monthly.csv"
YEARS = range(1997, 2027)

def pull_year(year: int) -> pd.DataFrame:
    """Stream one year's file, keep only iron ore rows."""
    chunks = pd.read_csv(
        BASE_URL.format(year=year),
        sep=";", encoding="latin-1",
        usecols=["CO_ANO", "CO_MES", "CO_NCM", "KG_LIQUIDO"],
        dtype={"CO_NCM": str},
        chunksize=500_000,
    )
    kept = [c[c["CO_NCM"].str.startswith("2601")] for c in chunks]
    df = pd.concat(kept)
    print(f"{year}: {len(df)} iron ore rows")
    return df

if __name__ == "__main__":
    frames = [pull_year(y) for y in YEARS]
    df = pd.concat(frames)
    df["month"] = pd.to_datetime(
        dict(year=df["CO_ANO"], month=df["CO_MES"], day=1)
    )
    monthly = (df.groupby("month")["KG_LIQUIDO"].sum() / 1_000).rename("tonnes")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    monthly.to_csv(OUT_PATH)
    print(f"\n{len(monthly)} months, {monthly.index.min():%Y-%m} to {monthly.index.max():%Y-%m}")
    print("\nAnnual totals (Mt), sanity check vs ~350-400 Mt/yr recently:")
    print((monthly.resample("YS").sum() / 1e6).tail(5).round(1))