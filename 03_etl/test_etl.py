import pandas as pd
from etl import process_large_csv
import os

def test_process_large_csv():
    df = pd.DataFrame({
        'category': ['A', 'B'] * 50000,
        'amount': range(100000)
    })
    df.to_csv('test_data.csv', index=False)
    result = process_large_csv('test_data.csv')
    assert len(result) == 2
    os.remove('test_data.csv')
