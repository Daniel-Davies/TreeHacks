
import numpy as np 
from sklearn im, decomposition
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def read_csv(file_name):
    data_X = np.genfromtxt(file_name, delimiter="\t", dtype = float, usecols = range(1, 101))
    data_Y = np.genfromtxt(file_name, delimiter="\t", dtype = str, usecols = (0))
    return data_X, data_Y

data_path = sys.argv[1] #train.csv
demo_path = sys.argv[2] #does not need to be read in, should be output from processing the demo

data_X, data_Y = read_csv(data_path)


demo = np.loadtxt(demo_path, delimiter ="\t", dtype = str)


np.random.seed(1)

#ONLY NEEDED if demo is (100,)
demo = np.expand_dims(demo, axis = 0)

data_X = np.concatenate((data_X, demo), axis = 0)
data_Y = np.concatenate((data_Y, np.array(["2"])))


pca = decomposition.PCA(n_components = 50)
results = pca.fit_transform(data_X)
tsne = manifold.TSNE(verbose = 1)
results = tsne.fit_transform(results)

results_bacteria = []
results_viral = []
results_demo = []
for index, value in enumerate(data_Y):
	if value == "0":
		results_bacteria.append(results[index])
	elif value == "1":
		results_viral.append(results[index])
	else:
		results_demo.append(results[index])
	
print(results_bacteria, results_viral, results_demo)

remove_indices = []
for i in range(len(data_Y)):
	if data_Y[i] == "0":
		if results[i][0] > -1.5:
			remove_indices.append(i)
	if data_Y[i] == "1":
		if results[i][1] < 0:
			remove_indices.append(i)

data_Y = np.array([data for index, data in enumerate(data_Y) if index not in remove_indices])
results = np.array([data for index, data in enumerate(results) if index not in remove_indices])



plt.figure(figsize=(6, 5))
colors = 'b', 'g', 'r'
for i, c, label in zip(["0", "1", "2"], colors, data_Y):
    plt.scatter(results[data_Y == i, 0], results[data_Y == i, 1], c=c, label=label)
blue_patch = mpatches.Circle(1, color='b', label='Bacterial')
green_patch = mpatches.Circle(1, color='g', label='Viral')
red_patch = mpatches.Circle(1, color='r', label='Input')
plt.legend(handles=[blue_patch, green_patch, red_patch])
plt.show()


