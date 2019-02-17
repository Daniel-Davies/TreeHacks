import numpy as np 

def read_csv(file_name):
    data_X = np.genfromtxt(file_name, delimiter="\t", dtype = float, usecols = range(1, 101))
    data_Y = np.genfromtxt(file_name, delimiter="\t", dtype = str, usecols = (0))
    return data_X, data_Y


demo_path = "demo_output_b1.csv" #does not need to be read in, should be output from processing the demo
demo = np.loadtxt(demo_path, delimiter ="\t", dtype = str) #not needed 


data_path = "train.csv"
gene_path = "gene_order.csv"
viral_file = "virus_only.txt"
bac_file = "bac_only.txt"

data_X, data_Y = read_csv(data_path)
gene_order = np.loadtxt(gene_path, delimiter = "\t", dtype = str).tolist()
bac_genes = np.loadtxt(bac_file, delimiter = ",", dtype = str)
viral_genes = np.loadtxt(viral_file, delimiter = ",", dtype = str)

print(len(bac_genes) + len(viral_genes))
bac_indices = [gene_order.index(gene) for gene in bac_genes]
viral_indices = [gene_order.index(gene) for gene in viral_genes]

indices_order_cols = viral_indices + bac_indices

#rows are genes
data = data_X.T

data_sorted_genes = np.array([data[index] for index in indices_order_cols]).T

bac_train_indices = [index for index, value in enumerate(data_Y) if value == "0"]

viral_train_indices = [index for index, value in enumerate(data_Y) if value == "1"]
indices_order_rows = viral_train_indices + bac_train_indices 

data_sorted_train = np.array([data_sorted_genes[index] for index in indices_order_rows])

np.savetxt("heatmap_train.csv", data_sorted_train, fmt="%s", delimiter = "\t")
np.savetxt("heatmap_sort_indices", indices_order_cols, fmt="%s", delimiter = "\t")

print("bac train", len(bac_train_indices))
print("viral train", len(viral_train_indices))
print("bac gene", len(bac_indices))
print("viral gene", len(viral_indices))

#sort demo 


demo_path = "demo_output_b1.csv" #does not need to be read in, should be output from processing the demo
demo = np.loadtxt(demo_path, delimiter ="\t", dtype = str) #not needed 


indices_order_cols = np.loadtxt("heatmap_sort_indices", delimiter = "\t", dtype = int)
train_sorted = np.loadtxt("heatmap_train.csv", delimiter = "\t", dtype = float)
demo = [demo[index] for index in indices_order_cols]

demo = np.expand_dims(demo, axis = 0)

heatmap_values = np.concatenate((train_sorted, demo), axis = 0)








