from django.shortcuts import render,redirect
from . models import Services,MyModel


def AddService(request):
    services=Services.objects.all()
    if request.method == 'POST':
        mymodel = MyModel()
        name = request.POST.get('name')
        msg = request.POST.get('msg')
        email = request.POST.get('email')
        mymodel.name = name
        mymodel.msg = msg
        mymodel.email = email
        mymodel.save()
        return redirect('/')
    return render(request,'index.html',{'services':services})

