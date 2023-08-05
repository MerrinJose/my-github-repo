from django.shortcuts import render
from . models import Place,Chefs

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=Chefs.objects.all()
    return render(request, 'index.html', {'object': obj, 'object2': obj2})
