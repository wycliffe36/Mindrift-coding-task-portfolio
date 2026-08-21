import pandas as pd
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from etl import transform_csv

def test_transform_csv():
    df = pd.DataFrame({'price':[10,20],'quantity':[2,3]})
    df.to_csv('test_data.csv', index=False)
    transform_csv('test_data.csv', 'test_out.csv')
    result = pd.read_csv('test_out.csv')
    assert len(result) == 2
    assert 'total' in result.columns
    assert result['total'].tolist() == [20, 60]
    os.remove('test_data.csv')
    os.remove('test_out.csv')
