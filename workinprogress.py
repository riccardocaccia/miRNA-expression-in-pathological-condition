import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# data loading
file_path = ##path to data
data = pd.read_csv(file_path, sep='\t', comment='!', index_col=0)

# data first exploratiom
print(data.shape)  
print(data.head())  

# cleaning NA
data_clean = data.dropna()

# Visualization and Heatmap of first 50 miRNA
plt.figure(figsize=(10, 8))
sns.heatmap(data_clean.iloc[:50, :], cmap='viridis')
plt.title('Expression Heatmap')
plt.xlabel('Sample')
plt.ylabel('miRNA')
plt.show()

...
