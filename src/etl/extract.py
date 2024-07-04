import pandas as pd

file_path = ("/Users/nathan/Projects/animal_viz/data/raw/yearly_slaughter_weight.xlsx")
df = pd.read_excel(file_path)
df = df.iloc[9:19]
df = df[['Unnamed: 0', 'Unnamed: 2', 'Unnamed: 4', 'Unnamed: 6', 'Unnamed: 8']]
df.rename(columns={
    'Unnamed: 0': 'year',
    'Unnamed: 2': '<1.4',
    'Unnamed: 4': '1.4 < 2.7',
    'Unnamed: 6': '>2.7',
    'Unnamed: 8': 'Total_chicken_death'
}, inplace=True)