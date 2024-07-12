from django.shortcuts import render
from . forms import Student
# Create your views here.
def home(request):
    if request.method=='POST':
        form=Student(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'home.html',{'form':form})
    else:
        form=Student(request.POST)
    return render(request,'home.html',{'form':form})


def link(request):
    return render(request,'link.html')   
