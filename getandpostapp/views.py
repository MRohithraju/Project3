from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getinput(request):
    return render(request,"getinput.html")
def getadd(request):
    i=request.GET["t1"]
    j=request.GET["t2"]
    try:
        x=int(i)
        y=int(j)
        k=x+y
        return HttpResponse("the sum of:"+str(k))
    except(ValueError):
        return HttpResponse("invalid input")
def postinput(request):
    return render(request,"postinput.html")
def postadd(request):
    i=request.POST["t1"]
    j=request.POST["t2"]
    try:
        x=int(i)
        y=int(j)
        k=x+y
        return HttpResponse("the sum is:"+str(k))
    except(ValueError):
        return render("invalid input")



