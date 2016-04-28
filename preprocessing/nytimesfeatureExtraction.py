#sentiment, duck duck go results and summary aggregrated per month & combining with Google Trends
import glob,json,csv
from textblob import TextBlob
import json
import pandas as pd
from PageRankSummarizer import PageRankSummarizer
import nltk
pageRankSummarizer = PageRankSummarizer()

f = open('socialList.txt', 'r')
df=pd.read_csv('../googletrends_month_aggregated.csv', sep=",") #this file has been generated using pandas on the command line from the aggregated google trends
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

url = "https://duckduckgo.com/html/?q="  # THe query will be appended to this


for file in x:
	name=file.split("/")[1].split("\n")[0].lower().strip() 
	if name not in names:
		print file
		continue;
	try:
		google=df[name]
	except:
		print name +"googl" #check if there is google trend result
		continue
	f=open ("dates.txt");
	for data in f:
		
		values[data.strip()]={"text":"","ny_count":0,"sentiment":0,"keywords":{},"google_trend_count":df[name][data.strip()]}
		months.append(data.split("/")[1]);

	f=open(file) #open the movement article file for this name
	r=json.loads(f.read())
	print name

	for data in r:
		split=data["pub_date"].split("-")
		key=str(int(split[1]))+"/"+months[int(split[1])-1]+"/"+split[0][2:]
		if (data["abstract"]):
			text=data["abstract"] #check if abstract exists
		elif data["lead_paragraph"]:
			text=data["lead_paragraph"] #If not check if lead paragraph exists
		else :
			try:
				text=data["headline"]["main"] #If not check if headline and its main exist
			except:
				text="" #If not append nothing

		blob_file_content = TextBlob(text)
		

		
		try:
			values[key]["text"]+=text+"\n";
			values[key]["ny_count"]+=1;
			values[key]["sentiment"]+=blob_file_content.sentiment.polarity #calcualte polarity
			for words in data["keywords"]:
					if words["value"] not in values[key]["keywords"]: #append keywords
						values[key]["keywords"][words["value"]]=0
					values[key]["keywords"][words["value"]]+=1
		except:
			if (int(split[1])==2):
				key=str(int(split[1]))+"/28/"+split[0][2:] #date for Febraury

				values[key]["text"]+=text+"\n";
				values[key]["ny_count"]+=1;
				values[key]["sentiment"]+=blob_file_content.sentiment.polarity
				for words in data["keywords"]:
					if words["value"] not in values[key]["keywords"]:
						values[key]["keywords"][words["value"]]=0
					values[key]["keywords"][words["value"]]+=1
			else:
				print key
	results=[]
	for val in values:
		sentimentSum=0
		if (values[val]["ny_count"])>0:
			sentimentSum=values[val]["sentiment"]/values[val]["ny_count"]*1.0 #Get overall sentiment

		keywords=sorted(values[val]["keywords"], key=values[val]["keywords"].get,reverse=True) #Get list of all keywords sorted in frequency order
		summary=""
		resultLine=values[val]["text"]
		if(resultLine):
			resultLine=resultLine.replace(";"," . ")
			resultLine=nltk.sent_tokenize(resultLine)
			if len(resultLine)>1000: #avoid more than 1000 lines to calculate summary to speed up process
				resultLine=resultLine[:1000]
			try:
				summary=pageRankSummarizer.summarize(resultLine, 1)[0] #calculate 1 line summary
			except:
				summary=resultLine[0]
				print "--------"

		results.append({'date':val,"ny_count":values[val]["ny_count"],
		 "sentiment":sentimentSum,"keywords":keywords[:4],"google_trend_count":values[val]["google_trend_count"],"summary":summary})

	r = duckduckgo.query(name) #Get the duckduck go results
	try:
		definition=r.related[1].text 
	except:
		print "none"+name
		definition="$"
	resultant.append({"name":name,"values":results,"definition":definition})
	

print len(resultant)
with open('movement.json', 'w') as outfile:
	json.dump(resultant, outfile)
