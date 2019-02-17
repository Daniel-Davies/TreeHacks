from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.mail import send_mail
import json
from django.http import JsonResponse
from django.http import HttpResponse
from joblib import load
from sklearn import svm, manifold, decomposition
import pickle
import numpy as np

from .utils import file_to_gsea

# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'DocOc/index.html')

@csrf_exempt
def sendMail(request):
    if request.method == 'POST':
        data = request.POST.get("emailEntry")
        send_mail('Subject here','Here is the message.','callmedanemailacc@gmail.com',[data],fail_silently=False)
        return render(request, 'DocOc/dashboard.html')
    else:
        return render(request, "DocOc/breakdown.html")

@csrf_exempt
def entry(request):
    return render(request, 'DocOc/entry.html')

@csrf_exempt
def breakdownViral(request):
    return render(request, 'DocOc/breakdownViral.html')

@csrf_exempt
def dashboard(request):
    return render(request, 'DocOc/dashboard.html')

@csrf_exempt
def verdict(request):
    return render(request, 'DocOc/verdict.html')

@csrf_exempt
def breakdown(request):
    return render(request, 'DocOc/breakdown.html')

@csrf_exempt
def upload(request):


    results_bacteria = []
    results_viral = []
    results_demo = []    
    result = -1
    geneData = []
    flatmap_vals = []

    # if this is a POST request we need to process the form data
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        geneData = file_to_gsea(str(myfile))
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # create a form instance and populate it with data from the request:
        
        # Data preprocessing
        demo_path = uploaded_file_url
        mean_path = "DocOc/static/train_mean.csv"
        std_path = "DocOc/static/train_std.csv"
        genes_path = "DocOc/static/gene_order.csv"

        #demo should have first row be gene name and second row be value 
        demo = np.loadtxt(demo_path, delimiter ="\t", dtype = str) #(2, 13321)
        mean = np.loadtxt(mean_path, delimiter ="\t", dtype = float) #(100,)
        std = np.loadtxt(std_path, delimiter ="\t", dtype = float) #(100,)
        genes = np.loadtxt(genes_path, delimiter ="\t", dtype = str) #(100,)

        demo_dict = {}
        for gene, value in demo.T:
            demo_dict[gene.upper()] = float(value)

        data = np.array([demo_dict[gene] if gene in demo_dict else mean[index] for index, gene in enumerate(genes)])

        data = (data - mean) / std
        data = np.expand_dims(data,axis=0)

        # loading the model
        clf = load('DocOc/static/trained_svm.joblib')

        # predicting output
        result = clf.predict(data)

        # scatter plot data stuff
        file_name = "DocOc/static/train_scatter.csv"
        data_X = np.genfromtxt(file_name, delimiter="\t", dtype = float, usecols = range(1, 101))
        data_Y = np.genfromtxt(file_name, delimiter="\t", dtype = str, usecols = (0))
        
        data_X = np.concatenate((data_X, data), axis = 0)
        data_Y = np.concatenate((data_Y, np.array(["2"])))
        np.random.seed(2)
        pca = decomposition.PCA(n_components = 50)
        results = pca.fit_transform(data_X)
        tsne = manifold.TSNE(verbose = 1)
        results = tsne.fit_transform(results)

        for index, value in enumerate(data_Y):
            if value == "0":
                results_bacteria.append(results[index].tolist())
            elif value == "1":
                results_viral.append(results[index].tolist())
            else:
                results_demo.append(results[index].tolist())
        # heat map stuff
        indices_order_cols = np.loadtxt("DocOc/static/heatmap_sort_indices", delimiter = "\t", dtype = int)
        train_sorted = np.loadtxt("DocOc/static/heatmap_train.csv", delimiter = "\t", dtype = float)

        data = [data[0][index] for index in indices_order_cols]        
        data = np.expand_dims(data, axis = 0)
        _sorted = np.concatenate((train_sorted[:5],train_sorted[-5:]),axis=0)

        heatmap_values = np.concatenate((_sorted, data), axis = 0).T

        
        for index,row in enumerate(heatmap_values):
            for i2, col in enumerate(row):
                flatmap_vals.append([index,i2,col])


    return render(request, 'DocOc/verdict.html',{'result': result,'x_scatter_data': results_bacteria,'y_scatter_data':results_viral,'z_scatter_data':results_demo, 'geneData': geneData,'heatmap_data':flatmap_vals})


@csrf_exempt
def forums(request):
    return render(request,"DocOc/forums.html")


@csrf_exempt
def about(request):
    return render(request,"DocOc/about.html")


@csrf_exempt
def tracking(request):
    return render(request,"DocOc/tracking.html")