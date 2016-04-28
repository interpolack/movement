#Merge all the google trend csvs
import pandas as pd
import os
f = open('socialList.txt', 'r')
names=[]
for data in f:
	names.append(data.strip())
print len(names)
i=0
for name in names:
	try:
		df1 = pd.read_csv("newgoogletrends.csv")
		df2 = pd.read_csv("googlefiles/"+name+".csv",skiprows=4,nrows=640)
		merged = df1.merge(df2, on="Week", how="outer").fillna("")
		merged.to_csv("newgoogletrends.csv", index=False)
		i+=1;
	except:
		print name
		
print i