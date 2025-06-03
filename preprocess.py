

import pandas as pd
import osgb

fff = "mapno22023.csv"
df = pd.read_csv(fff)
print(df)

print("update")


print(df)

print("update again")

#  https://stackoverflow.com/questions/16476924/how-can-i-iterate-over-rows-in-a-pandas-dataframe
df['latitude'] = df.apply(lambda row: osgb.grid_to_ll(row['x'], row['y'])[0], axis=1)
df['longitude'] = df.apply(lambda row: osgb.grid_to_ll(row['x'], row['y'])[1], axis=1)

df = df.rename(columns={"no22023": "scalar_value" })

print(df)

fff = 'data.csv'
df.to_csv(fff , index=False)

print("Written to csv file " , fff )

