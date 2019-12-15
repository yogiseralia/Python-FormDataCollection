from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def data_collect(request):
    fdata = request.GET.get('text','EMPTY')
    print(fdata)
    return HttpResponse("Data Collected!")
