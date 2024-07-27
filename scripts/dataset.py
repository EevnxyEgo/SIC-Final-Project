import pandas as pd
import numpy as np

# make fictitious data
np.random.seed(42) 
data = {
    'temperature': np.random.uniform(20, 40, 100000),  
    'humidity': np.random.uniform(20, 100, 100000),
    'airQuality': np.random.uniform(300, 2000, 100000),
    'asthma_attack': np.random.choice([0, 1], 100000, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# sinpan dataset
df.to_csv('../data/asthma_dataset.csv', index=False)
