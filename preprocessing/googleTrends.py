#Get csvs per google trend
from pytrends.pyGTrends import pyGTrends
import time
from random import randint

google_username = "" #username removed before uploading
google_password = "" #password removed before uploading
path=""

# connect to Google
connector = pyGTrends(google_username, google_password)
# make request
f = open('socialList.txt', 'r')
i=0
query=""
for data in f:
	i+=1;
	query=data.strip()
	print "query:"+ query
	connector.request_report(query,geo="US")
	# wait a random amount of time between requests to avoid bot detection
	time.sleep(randint(5, 10))
	connector.save_csv(path,query)
	time.sleep(randint(5, 10))
# get suggestions for keywords
