#calculate the summary of ny times permonth
import glob,json,csv
from textblob import TextBlob
import json
import pandas as pd
from PageRankSummarizer import PageRankSummarizer
import nltk
pageRankSummarizer = PageRankSummarizer()
f = open('../newMovement.txt', 'r')
df=pd.read_csv('../googletrends_month_aggregated.csv', sep=",")
df=df.set_index("month")
names=[]
for data in f:
	names.append(data.strip().lower())

x=glob.glob('./*.json')

values={}
months=[]

resultant=[]

keywordsCorpus=[];
import duckduckgo

url = "https://duckduckgo.com/html/?q="  # change to whatever your url is


for file in x:
	name=file.split("/")[1].split("\n")[0].lower().strip()
	if name not in names:
		print ""
		continue;
	try:
		google=df[name]
	except:
		print ""
		continue
	f=open ("dates.txt");
	for data in f:
		
		values[data.strip()]={"text":""}
		months.append(data.split("/")[1]);

	f=open(file)
	r=json.loads(f.read())
	print name

	for data in r:
		split=data["pub_date"].split("-")
		key=str(int(split[1]))+"/"+months[int(split[1])-1]+"/"+split[0][2:]
		if (data["abstract"]):
			text=data["abstract"]
		elif data["lead_paragraph"]:
			text=data["lead_paragraph"]
		else :
			try:
				text=data["headline"]["main"]
			except:
				text=""
		
		try:
			values[key]["text"]+=text+"\n";
		except:
			if (int(split[1])==2):
				key=str(int(split[1]))+"/28/"+split[0][2:]

				values[key]["text"]+=text+"\n";
			else:
				print ""
	results=[]
	for val in values:
		summary=""
		resultLine=values[val]["text"]
		if(resultLine):
			resultLine=resultLine.replace(";"," . ")
			resultLine=nltk.sent_tokenize(resultLine)
			if len(resultLine)>500:
				resultLine=resultLine[:500]
			try:
				summary=pageRankSummarizer.summarize(resultLine, 1)[0]
			except:
				summary=resultLine[0]
				print "--------"
		results.append({'date':val,"summary":summary})
	
	resultant.append({"name":name,"values":results})
	
	

print len(resultant)
with open('summary.json', 'w') as outfile:
	json.dump(resultant, outfile)
quit()
