import numpy as np
from sklearn import svm, metrics
from sklearn.metrics import mean_squared_error
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from scipy import stats
from sklearn.svm import SVC
from joblib import dump

def read_csv(file_name):
    data_X = np.genfromtxt(file_name, delimiter="\t", dtype = float, usecols = range(1, 101))
    data_Y = np.genfromtxt(file_name, delimiter="\t", dtype = str, usecols = (0))
    return data_X, data_Y

train_X, train_Y = read_csv("train.csv")
test_X, test_Y = read_csv("test.csv")


parameters = {'C': [10**e for e in range(-3, 4)], 'gamma' : [10**e for e in range(-3, 4)]} #change parameters to search over 
svc = svm.SVC(kernel = 'rbf') #change kernel 
clf = GridSearchCV(svc, parameters, scoring = 'accuracy', n_jobs=10, cv=5, verbose = 1) #change scoring between accuracy, f1, roc_auc
clf.fit(train_X, train_Y)
param_dict = clf.best_params_
print(clf.best_params_)
print(clf.best_score_)

#TEST PERFORMANCE based on gamma, C from grid search 
clf = SVC(gamma= param_dict["gamma"], C= param_dict["C"])
clf.fit(train_X, train_Y)
print(test_X.shape)
dump(clf, 'trained_svm.joblib') 
y_pred = clf.predict(test_X)
print(y_pred)
print(test_Y)
