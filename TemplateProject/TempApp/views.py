from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'text':'hello world', 'number':100}
    return render(request,"TempApp/index.html",context_dict)

def other(request):
    return render(request,"TempApp/other.html")

def relative(request):
    return render(request,"TempApp/relative_url_templates.html")
