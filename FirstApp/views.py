from django.shortcuts import render, HttpResponse
from FirstApp.models import personinfo

# Create your views here.
def index(request):
    if request.method == "POST":
        n = request.POST['idname']
        e = request.POST['idemail']
        p = request.POST['idphone']
        c = request.POST['idcomment']
        ins=personinfo(name=n, email=e, phone=p, comment=c)
        ins.save()

   
    return render(request, 'index.html')

def about(request):
    
    return render(request, 'about.html')

def services(request):
   
    return render(request, 'services.html')

def contact(request):
   
    return render(request, 'contact.html')

def home(request):
   
    return render(request, 'index.html')