import numpy as np
import sys

demo_path = sys.argv[1]
mean_path = sys.argv[2]
std_path = sys.argv[3]
genes_path = sys.argv[4]

#demo should have first row be gene name and second row be value 
demo = np.loadtxt(demo_path, delimiter ="\t", dtype = str) #(2, 13321)
mean = np.loadtxt(mean_path, delimiter ="\t", dtype = float) #(100,)
std = np.loadtxt(std_path, delimiter ="\t", dtype = float) #(100,)
genes = np.loadtxt(genes_path, delimiter ="\t", dtype = str) #(100,)

demo_dict = {}
for gene, value in demo.T:
	demo_dict[gene.upper()] = float(value)

data = np.array([demo_dict[gene] if gene in demo_dict else mean[index] for index, gene in enumerate(genes)])

print(data)
data = (data - mean) / std


