from django.shortcuts import render

# Create your views here.
def html1(request):
    return render(request,'htmlfile.html')

def html2(request):
    return render(request,'htmlfile1.html')