import sys
import numpy as np

matrix_path = sys.argv[1]
score_path = sys.argv[2]

#matrix is originally (13322, 99), rows are genes, columns are people
#first line is label, first two columns are gene and gene description
matrix = np.loadtxt(matrix_path, delimiter ="\t", dtype = str, skiprows=2)

genes = np.loadtxt(score_path, usecols = (6), skiprows = 1, dtype = str)
genes = np.array([gene.lower() for gene in genes if "/" not in gene])

unique_top_genes = []
for gene in genes:
	if len(unique_top_genes) == 118:
		break
	if gene not in unique_top_genes:
		unique_top_genes.append(gene)


labels = matrix[0] #(97,)
remove_indices = []
for index, label in enumerate(labels):
	if "Healthy" in label:
		remove_indices.append(index) #remove the six Healthy patients


#0 is bacterial, 1 is viral, becomes shape (91, 1)
labels = labels[2:]
labels_binary = np.array([1 if "Influenza" in label else 0 for label in labels])
labels_binary = np.array([label for index, label in enumerate(labels_binary) if index not in remove_indices])
#labels_binary = np.expand_dims(labels_binary, axis = 1)


#matrix becomes (13322, 93), removed columns corresponding to healthy people
matrix = np.array([row for index, row in enumerate(matrix.T) if index not in remove_indices]).T

#rows correspond to top 100 genes that are in both unique_top_genes and matrix
matrix_used = np.array([row[2:] for row in matrix if row[0].lower() in unique_top_genes])
genes_used = np.array([row[0] for row in matrix if row[0].lower() in unique_top_genes])

#rows are people, columns are genes, shape = (91, 100)
matrix_used = np.array(matrix_used).T 

#rows are people, with remaining columns as genes
test = np.array([row for index, row in enumerate(matrix_used) if index in [0, 1, 13, 25]]).astype(float)
print(test)

#MAKE DEMOS
test_full = np.array([row for index, row in enumerate(matrix.T) if index - 2 in [0, 1, 13, 25]])
all_genes = np.array([row[0] for row in matrix])

all_genes = np.expand_dims(all_genes[1:], axis = 0)
test_demo = np.expand_dims(test_full[3][1:], axis = 0)

demo =  np.concatenate((all_genes, test_demo), axis = 0)
np.savetxt("demo_viral_2.csv", demo, fmt="%s", delimiter = "\t")


#MAKE TRAIN/TEST
train = np.array([row for index, row in enumerate(matrix_used) if index not in [0, 1, 13, 25]]).astype(float)

train_mean = np.mean(train, axis = 0)
train_std = np.std(train, axis = 0)

train = (train - train_mean) / train_std
test = (test - train_mean) / train_std

train = train.astype(str)
test = test.astype(str)

test_label = np.array([row for index, row in enumerate(labels_binary) if index in [0, 1, 13, 25]])
train_label = np.array([row for index, row in enumerate(labels_binary) if index not in [0, 1, 13, 25]])

test_label = np.expand_dims(test_label, axis = 1)
train_label = np.expand_dims(train_label, axis = 1)


together_train = np.concatenate((train_label, train), axis = 1)
together_test = np.concatenate((test_label, test), axis = 1)

np.savetxt("train.csv", together_train, fmt="%s", delimiter = "\t")
np.savetxt("test.csv", together_test, fmt="%s", delimiter = "\t")
np.savetxt("gene_order.csv", genes_used, fmt="%s", delimiter = "\t")
np.savetxt("train_mean.csv", train_mean, fmt="%s", delimiter = "\t")
np.savetxt("train_std.csv", train_std, fmt="%s", delimiter = "\t")

 


