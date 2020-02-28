########## PANDAS AND CSV ###########
import pandas as pd
from pandas import read_csv

df = pd.DataFrame(pd.read_csv("train_emoji.csv", sep = ',', encoding = "ISO-8859-1", index_col=0)) # use \t in case of TSV
df = pd.DataFrame(pd.read_csv("twitter/train.csv", sep = ',', encoding = "ISO-8859-1", index_col=0, names=["tag", "id", "date", "query", "user", "text"])) # use \t in case of TSV

df.head()

df[:10]

df['text']

list(df['text'])

df[['text', 'value']]

# drop duplicates
df = df.drop_duplicates(subset='text', keep="first")

# select specific
df.loc[df['value'] == '3']
df.loc[df['value'] > 0]

# concat dataframes
pd.concat([x,y], ignore_index=True)

# looping
df['processed_text'] = ''

for index, row in df.iterrows():
	df.at[index, 'text'] = preprocess(row['text'])

df['processed_text'] = df.apply(lambda row: preprocess(row['text']),axis=1)

# resetting index if need be
reset_index(drop=True)

