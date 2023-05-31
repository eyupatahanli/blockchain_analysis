import pandas as pd

df = pd.read_csv("/Users/eyupburakatahanli/Desktop/Github/stalking/export-address-token-0x2FfE5eF40fD39Da23E61Ebef4b68E15fF9843061.csv")

pd.set_option("display.max_columns",5)
pd.set_option("display.max_rows",None)
df.tail()

df.info()

type(df["UnixTimestamp"][1])

df["To"].value_counts()


df["From"].value_counts()

a = df["To"]

a.head()

d = a.reset_index().rename(columns={"index": "ID"})
d.head()

b = a.reset_index()
a.index()
c = a.reset_index().rename(columns={"index": "RowNumber"})
c