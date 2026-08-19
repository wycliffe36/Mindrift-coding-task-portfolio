import pandas as pd

def process_large_csv(filepath):
    df = pd.read_csv(filepath)
    result = df.groupby('category')['amount'].sum()
    return result
