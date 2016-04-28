#Generate all nytimes movements data files
import requests
import json
f = open('../socialList.txt', 'r')
i=0
query=""

for q in f:
	print q

	url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q="'+q.strip()+'"&facet_field=section_name&begin_date=20040101&end_date=20160401&api-key='+key
	response = requests.get(url)
	jsonData=json.loads(response.text)
	pages=(jsonData['response']['meta']['hits'])/10
	result=jsonData['response']['docs']
	print pages
	for page in xrange(1,pages):
		url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q="'+q.strip()+'"&facet_field=section_name&begin_date=20040101&end_date=20160401&api-key='+key+'&page='+str(page)
		try:
			print url
			response = requests.get(url)
			jsonData=json.loads(response.text)
			result=result+jsonData['response']['docs']
		except:
			print "error"
	output = open(q+'.json', 'w')
	output.write(json.dumps(result))