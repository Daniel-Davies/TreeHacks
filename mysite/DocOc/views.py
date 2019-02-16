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
from sklearn import svm
import pickle
import numpy as np


# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'DocOc/index.html')

@csrf_exempt
def sendMail(request):
    send_mail('Subject here','Here is the message.','callmedanemailacc@gmail.com',['daviesdg@uci.edu'],fail_silently=False)
    return render(request, 'DocOc/breakdown.html', {'confirmed': 1})

@csrf_exempt
def entry(request):
    return render(request, 'DocOc/entry.html')

@csrf_exempt
def dashboard(request):
    return render(request, 'DocOc/dashboard.html')

@csrf_exempt
def verdict(request):
    return render(request, 'DocOc/verdict.html')

@csrf_exempt
def breakdown(request):
    return render(request, 'DocOc/breakdown.html', {'confirmed': 0})

@csrf_exempt
def upload(request):
    result = -1
    # if this is a POST request we need to process the form data
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
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

    return render(request, 'DocOc/verdict.html',{'result': result})


@csrf_exempt
def forums(request):
    return render(request,"DocOc/forums.html")


@csrf_exempt
def about(request):
    return render(request,"DocOc/about.html")


@csrf_exempt
def tracking(request):
    return render(request,"DocOc/tracking.html")