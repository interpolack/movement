#Merge all the files generated from nytimes Trend
import glob,json,csv
x=glob.glob('./*.json')
f=open ("dates.txt");
values={}
months=[]
for data in f:
	values[data.strip()]=0
	months.append(data.split("/")[1]);
print values
print months
for file in x:
	f=open(file)
	r=json.loads(f.read())
	name=f.name.split("/")[1].split("\n")[0].lower().strip()
	print name
	for data in r:
		split=data["pub_date"].split("-")
		key=str(int(split[1]))+"/"+months[int(split[1])-1]+"/"+split[0][2:]
		try:
			values[key]+=1;
		except:
			if (int(split[1])==2):
				key=str(int(split[1]))+"/28/"+split[0][2:]
				values[key]+=1;
			else:
				print key
		
	writer = csv.writer(open('csv/'+name+'.csv','w'))
	writer.writerow(['month',name+"nytimes"])
	for key, value in values.items():
		writer.writerow([key, value])
	writer.writerow(["count",len(r)])