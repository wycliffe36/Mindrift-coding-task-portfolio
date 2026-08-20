import pandas as pd
import sys
sys.path.insert(0, '../03_etl')
from etl import transform_csv

if __name__ == "__main__":
    print("Docker container running ETL...")
    transform_csv("../data/large.csv", "output.csv")
    print("Done! Check output.csv")
