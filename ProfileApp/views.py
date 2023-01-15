from django.shortcuts import render,HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("<h1>hello world <br> This is My Web</h1>")

def firstweb(request):
    return render(request,'firstweb.html')

def secondpage(request):
    return render(request,'secondpage.html')

def thirdpage(request):
    return render(request,'thirdpage.html')

def home(request):
    return render(request,'home.html')

def product(request):
    return render(request,'product.html')
def idol(request):
    return render(request,'idol.html')

def hny(request):
    return render(request,'hny.html')