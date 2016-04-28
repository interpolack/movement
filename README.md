# movement
Piecing social movements together by their junctures, demonstrating how individual social movements can be interpreted as components of an encompassing narrative.

_data procuration `preprocessing/...`_
* Wikipedia's [List of social movements](https://en.wikipedia.org/wiki/List_of_social_movements) is used to seed the initial movement keywords in `socialList.txt`
* [pytrends](https://github.com/GeneralMills/pytrends) is used in `googleTrends.py` to retrieve [Google Trends](https://www.google.com/trends/) by keyword
* the [New York Times API](http://developer.nytimes.com/docs) is used in `nytimesTrends.py` to retrieve NYT articles by keyword

_data processing `preprocessing/...`_
* [Pandas](http://pandas.pydata.org/) is used to merge and read CSV files aggregated through `mergegoogletrends.py`
* [TextBlob](http://textblob.readthedocs.io/en/dev/) is used in `nytimesfeatureExtraction.py` for sentiment analysis of the aggregated NYT articles
* [DuckDuckGo](https://duckduckgo.com/) is scraped in `nytimesfeatureExtraction.py` to textual description of the aggregated NYT articles
* [NLTK](http://www.nltk.org/) is used in `nytimesfeatureExtraction.py` and `PageRankSummarizer.py` to tokenize strings
* [networkx](https://networkx.github.io/) is used in `PageRankSummarizer.py` for treating the sentences as a network
* [sklearn's feature_extraction] is used in `PageRankSummarizer.py` to extract the features from the text
* [scikit's PCA](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) is used in `reduction.py` to reduce trends into two dimensions

_data visualization `js/...`_
* [queue.js](https://github.com/d3/d3-queue) is used to read the data from the `data/*.json` files
* [d3.js](https://d3js.org/) is used to parse and render the data
* [jquery.selection.js](http://madapaja.github.io/jquery.selection/) is used to select text from the descriptions