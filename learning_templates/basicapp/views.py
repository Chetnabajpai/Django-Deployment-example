from django.shortcuts import render

def index(request):
    context_dict={'text':'My name is Chetna!', 'number':'21'}
    return render(request, "basicapp/index.html",context_dict)

def other(request):
    return render(request, "basicapp/other.html")

def relative(request):
    return render(request, "basicapp/relative.html")
