import pandas as pd

df = pd.read_csv('Merged_Stars.csv')
del df['Luminosity']


df.to_csv('pro130_data_cleaned_file.csv')