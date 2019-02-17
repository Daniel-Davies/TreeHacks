import numpy as np 

antibiotics = []
with open("megares_annotations_v1.01.csv", "r") as file:
	file.readline()
	for line in file:
		val = line.split(",")[1]
		antibiotics.append(val)


antibiotics = np.array(antibiotics)
antibiotics = np.unique(antibiotics)
print(antibiotics)
np.savetxt("unique_antibiotics.txt", antibiotics, fmt = "%s")

antibiotics = np.loadtxt("unique_antibiotics.txt", delimiter ="\t", dtype = str)
database = np.loadtxt("antibiotic_database.fasta", dtype = str)
fasta = np.loadtxt("demo_reads.fasta", dtype = str) #this will be the uploaded fasta file

labels = database[0::2]
seqs = database[1::2]
data_dict = {}
for index, label in enumerate(labels):
	seq = seqs[index]
	for a in antibiotics:
		if a.lower() in label.lower():
			data_dict[seq] = a
			break

resistant = []
fasta = fasta[1::2]
for seq  in fasta:
	if seq in data_dict:
		resistant.append(data_dict[seq])

resistant = np.unique(np.array(resistant))
print(resistant)




