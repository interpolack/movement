# movement
Piecing social movements together by their junctures, demonstrating how individual social movements can be interpreted as components of an encompassing narrative.

_data procuration_
* [Google Trends](https://www.google.com/trends/) was used to retrieve WSQ trends by keyword
* the [New York Times API](http://developer.nytimes.com/docs) was used to retrieve NYT articles by keyword

_data processing_
* [scikit's PCA](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) is used in `reduction.py` to reduce trends into two dimensions

_data visualization_
* [queue.js](https://github.com/d3/d3-queue) is used to read the data from the `data/*.json` files
* [d3.js](https://d3js.org/) is used to parse and render the data 
