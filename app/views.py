from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'Mihir','age':'24'}
    return render(request,'wish.html',context=d)

def condition(request):
    d={'a':10,'b':20}
    return render(request,'condition.html',context=d)
