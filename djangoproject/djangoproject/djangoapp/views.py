from django.shortcuts import render
from . models import Place


def demo(request):
    obj=Place.objects.all()
   # name="India"
    return  render(request,"index.html",{'result':obj})
#def addition(request):
#   x=int(request.GET['num1'])
#   y=int(request.GET['num2'])
#   res=x+y
#    mul=x*y
#   div=x/y

#   return render(request,"result.html", {'result':res,'subtraction':sub,'multiplication':mul,'division':div})




