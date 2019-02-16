from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.mail import send_mail

import sklearn

send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['daviesdg@uci.edu'],
    fail_silently=False,
)

# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'DocOc/index.html')

@csrf_exempt
def entry(request):
    return render(request, 'DocOc/entry.html')

@csrf_exempt
def verdict(request):
    return render(request, 'DocOc/verdict.html')

@csrf_exempt
def breakdown(request):
    return render(request, 'DocOc/breakdown.html')

@csrf_exempt
def upload(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # create a form instance and populate it with data from the request:

    return render(request, 'DocOc/verdict.html')
