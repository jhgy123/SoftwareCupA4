
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
        # return redirect(reverse("zya:index"))

def about(request):
    if request.method == "GET":
        return render(request, 'about.html')
        # return redirect(reverse("zya:about"))


def bhjc(request):
    if request.method == "GET":
        return render(request, 'bhjc.html')
        # return redirect(reverse("zya:bhjc"))

def mbjc(request):
    if request.method == "GET":
        return render(request, 'mbjc.html')
        # return redirect(reverse("zya:mbjc"))

def dwfl(request):
    if request.method == "GET":
        return render(request, 'dwfl.html')
        # return redirect(reverse("zya:dwfl"))

def mbtq(request):
    if request.method == "GET":
        return render(request, 'mbtq.html')
        # return redirect(reverse("zya:mbtq"))




def upload(request):
    return render(request, 'upload.html')

def ajaxtest(request):
    return render(request, 'ajaxtest.html')

def predicttest(request):
    return render(request, 'predict_test.html')