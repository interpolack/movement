import json
from collections import defaultdict
from sklearn.decomposition import PCA
import numpy

with open('data/movements.json') as f:
    movements = json.load(f)

instances = defaultdict(list)
for movement in movements:
    for value in movement['values']:
        split = value['date'].split('/')
        value['date'] = ((int(split[2]) - 4) * 12) + int(split[0])
    movement['values'] = sorted(movement['values'], key=lambda x: x['date'])
    for value in movement['values']:
        instances[movement['name']] += [value['google_trend_count']]

with open('data/trends.json', 'w') as f:
    json.dump(instances, f)

for movement in instances:
    instances[movement] = [float(value) / max(instances[movement]) for value in instances[movement]]
names = [key for key, value in instances.iteritems()]
instances = numpy.array([value for key, value in instances.iteritems()])
pca = PCA(n_components=2)
instances = pca.fit_transform(instances)

points = {}
for i, instance in enumerate(instances):
    points[names[i]] = instances[i].tolist()

for movement in points:
    print movement, points[movement]

with open('data/points.json', 'w') as f:
    json.dump(points, f)
