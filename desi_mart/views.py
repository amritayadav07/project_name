from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    params = {'name': request.GET.get('name','')}
    return render(request,'index.html',params)
def about(request):
    return HttpResponse("<h1>about us</h1>")
def contact(request):
    return HttpResponse("<h1>contact us</h1>")    