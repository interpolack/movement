import json
from collections import defaultdict
from sklearn.decomposition import PCA
import numpy

# load the movements.json data
with open('data/movements.json') as f:
    movements = json.load(f)

# represent each movement as a data instance
instances = defaultdict(list)
for movement in movements:
    # parse the movement date strings and sort them
    for value in movement['values']:
        split = value['date'].split('/')
        value['date'] = ((int(split[2]) - 4) * 12) + int(split[0])
    movement['values'] = sorted(movement['values'], key=lambda x: x['date'])
    # move the sorted values to the movement instance
    for value in movement['values']:
        instances[movement['name']] += [value['google_trend_count']]

# write the sorted trend values to trends.json
with open('data/trends.json', 'w') as f:
    json.dump(instances, f)

# normalize each instance's values
for movement in instances:
    instances[movement] = [float(value) / max(instances[movement]) for value in instances[movement]]
# keep track of each instance's movement name
names = [key for key, value in instances.iteritems()]
instances = numpy.array([value for key, value in instances.iteritems()])
# perform dimensionality reduction with PCA
pca = PCA(n_components=2)
instances = pca.fit_transform(instances)

# move the final component values to a dictionary format
points = {}
for i, instance in enumerate(instances):
    points[names[i]] = instances[i].tolist()

# print to make sure everything is okay
for movement in points:
    print movement, points[movement]

# write the final component values to points.json
with open('data/points.json', 'w') as f:
    json.dump(points, f)
