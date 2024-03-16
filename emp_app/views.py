from django.shortcuts import render,HttpResponse
from .models import Department,Employee,Role
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {'emps': emps}
    return render(request, 'all_emp.html',context)

def add_emp(request):
    if request.method =='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        salary = int(request.POST.get('salary'))
        bonus = int(request.POST.get('bonus'))
        dept = int(request.POST.get('dept'))
        role = int(request.POST.get('role'))
        phone = int(request.POST.get('phone'))
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, dept_id=dept, role_id=role, phone=phone,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added Successfully")
    elif request.method == 'GET':
        dept = Department.objects.all()
        roles = Role.objects.all()
        # dept_data={'dept' : dept}
        
        # role_data = {'role': roles}
    
        data = {
            'dept': dept,
            'role': roles
            }
        
        print(data)
        return render(request, 'add_emp.html',data)
    else:
        return HttpResponse('Exceptions Happens')
    
    
def remove_emp(request,emp_id = 0):
    if emp_id:
        try:
            emp_to_remove = Employee.objects.get(id=emp_id)
            emp_to_remove.delete()
            return HttpResponse('Employee Removed Successfully')
        except:
            return HttpResponse('Please Enter A Valid Employee ID')
            
    emps = Employee.objects.all()
    context = {'emps': emps}
    return render(request, 'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        emps = Employee.objects.all()
        
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)
            
        context = {
            'emps':emps
        }
        
        return render(request, 'all_emp.html',context)
    elif request.method == 'GET':
        dept = Department.objects.all()
        roles = Role.objects.all()
        # dept_data={'dept' : dept}
        
        # role_data = {'role': roles}
    
        data = {
            'dept': dept,
            'role': roles
            }
        
        return render(request, 'filter_emp.html',data)
    else:
        return HttpResponse('An Exception Occured')
    
