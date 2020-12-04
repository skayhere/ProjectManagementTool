from django.shortcuts import render,redirect
from .models import Employee, Project
from .forms import EmployeeForm, ProjectForm
from django.db.models import Q


# Create your views here.

def welcome(request):
    return render(request,"welcome.html")


def load_form(request):
    form = EmployeeForm
    return render(request, 'index.html', {'form':form})

def load_proj(request):
    form = ProjectForm
    return render(request, 'index.html', {'form':form})

def add(request):
    form = EmployeeForm(request.POST)
    form.save()
    return redirect('/show')

def addproj(request):
    form = ProjectForm(request.POST)
    form.save()
    return redirect('/showproj')

def show(request):
    employee = Employee.objects.all()
    return render(request, 'show.html', {'employee':employee})

def showproj(request):
    project = Project.objects.all()
    return render(request, 'showproj.html', {'project':project})

def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee':employee})

def editproj(request,id):
    project = Project.objects.get(id=id)
    return render(request, 'editproj.html', {'project':project})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    form.save()
    return redirect('/show')

def updateproj(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(request.POST, instance=project)
    form.save()
    return redirect('/showproj')

def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')

def deleteproj(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('/showproj')

def search(request):
    given_name =  request.POST['name']
    employee = Employee.objects.filter(Q(ename__icontains=given_name) | Q(lname__icontains=given_name))
    return render(request,'show.html', {'employee':employee})

def searchproj(request):
    proj_name =  request.POST['pname']
    project = Project.objects.filter(Q(ename__icontains=proj_name))
    return render(request,'showproj.html', {'project':project})

# def listproj(request):
#    agencys_sp = GPSpecial.objects.filter(agencys=32,is_active=True).values_list('agencys')
#    agencys_spe = [i[0] for i in agencys_sp]


# def selectview(request):
#    em  = Employee.objects.filter(ename__icontains=given_name)
#    form = request.POST 
#    if request.method == 'POST':
#       selected = get_object_or_404(Employee, pk=request.POST.get('em_id'))
#       ename.em = selected
#       ename.save()
#    return render(request,'show.html', {'employee':employee})

# def retrieve(request):
#     dataset = Employee.objects.filter(ename_icontains=given_name)
#     return render(request,'show.html',{'employee':employee})