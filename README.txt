1. Differentiation Between Viral vs. Bacterial Infections:

For machine-learning (SVM) to differentiate between viral and bacterial infections, we used MicroArray dataset GLP96 from:
Ramilo O, Allman W, Chung W, Mejias A et al. Gene expression patterns in blood leukocytes discriminate patients with 
acute infections. Blood 2007 Mar 1;109(5):2066-77. PMID: 17105821 

We used GEO2R to compare the bacterial infected datasets and viral infected datasets to get the top 100 differentially 
expressed genes. We then used the expression of these top differentially expressed genes for SVM.

We used sklearn to train our SVM. We do a logarithmic grid search from 10^-3 to 10^3 for tuning parameters C and gamma. We 
train using accuracy as our metric and by performing 5 fold cross validation in order to choose the best parameters. 
Our final parameters were C=1 and gamma=0.001. Our five fold cross validation had an accuracy of 90.8% and our test set had a 
100% accuracy.


2. Mapping bacterial genome to find antibiotic-resistance conferring genes

For our analysis, we used the Antibiotic Resistance Genes Database from:
Liu B, Pop M. ARDB-Antibiotic Resistance Genes Database. Nucleic Acids Res. 2009 Jan;37(Database issue):D443-7 
