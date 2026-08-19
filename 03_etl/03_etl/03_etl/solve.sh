#!/bin/bash
cat > etl.py << 'EOF'
import pandas as pd
def process_large_csv(filepath):
    chunks = []
    for chunk in pd.read_csv(filepath, chunksize=10000):
        chunks.append(chunk.groupby('category')['amount'].sum())
    result = pd.concat(chunks).groupby(level=0).sum()
    return result
EOF
