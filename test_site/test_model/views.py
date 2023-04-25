from django.shortcuts import render , redirect

from test_model.forms import carForm  
from test_model.models import car  

# Create your views here.


def form(request):  
    if request.method == "POST":  
        form = carForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('model/show')
            except Exception:
                pass
    else:  
        form = carForm()
    return render(request,"test_model/index.html",{'form':form})


## show the data base

def show(request):  
    employee = car.objects.all()  
    return render(request,"test_model/show.html",{'employee':employee})  


## Edit a record in the database
def edit(request, id):  
    employee = car.objects.get(id=id)  
    return render(request,"test_model/edit.html", {'employee':employee})  


## Update any record
def update(request, id):  
    employee = car.objects.get(id=id)  
    form = carForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, "test_model/edit.html", {'employee': employee})  

## destrot any record
def destroy(request, id):  
    employee = car.objects.get(id=id)  
    employee.delete()  
    return redirect("model/show")  