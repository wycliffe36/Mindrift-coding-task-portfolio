import pandas as pd
def transform_csv(input_path, output_path):
    chunks = []
    for chunk in pd.read_csv(input_path, chunksize=100000):
        chunk['total'] = chunk['price'] * chunk['quantity']
    chunks.append(chunk)
    df = pd.concat(chunks)
    df.to_csv(output_path, index=False)
