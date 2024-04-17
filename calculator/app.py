from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def calculator(request):
    c=""
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
            

    except:
        c="Invalid operator"
    print(c)
    return render(request, 'index.html',{"c":c})


def evenodd(request):
    d=''
    if request.method=='POST':
        n=eval(request.POST.get('value1'))
        if n%2==0:
            d = 'Even Number'
        else:
            d = 'Odd Number'
    return render(request, 'even-odd.html',{'d':d})