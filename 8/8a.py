from scipy.spatial.distance import pdist, squareform
import numpy as np
import pandas as pd
from math import prod

coords = [tuple(int(v) for v in line.split(",")) for line in open("input.txt", mode="r")]

points = np.array(coords)
distance_matrix = squareform(pdist(points, metric='euclidean'))
rows, cols = np.triu_indices_from(distance_matrix, k=1)
upper_distances = distance_matrix[rows, cols]
nearest_indices = upper_distances.argsort()[:1000]

circuits = []
for i in nearest_indices:
    box1 = int(cols[i])
    box2 = int(rows[i])
    print(box1, box2)
    box1_circuit = next((c for c in circuits if box1 in c), None)
    box2_circuit = next((c for c in circuits if box2 in c), None)
    if box1_circuit:
        if box2_circuit:
            if box2_circuit != box1_circuit:
                circuits.remove(box2_circuit)
            box1_circuit.update(box2_circuit)
        else:
            box1_circuit.add(box2)
    elif box2_circuit:
        if box1_circuit:
            if box1_circuit != box2_circuit:
                circuits.remove(box1_circuit)
            box2_circuit.update(box1_circuit)
        else:
            box2_circuit.add(box1)
    else:
        circuits.append(set([box1, box2]))

print(prod([len(c) for c in sorted(circuits, key=lambda c: len(c), reverse=True)[:3]]))
