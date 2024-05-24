from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee



# Create your views here.


def main(request):
    return render(request , "create.html")



def create(request):
    if request.method=="POST":
        print("Post")
        
        name=request.POST["name"]      #n
        salary=request.POST["salary"]  #s
        email=request.POST["email"]    #e
        
        emp=Employee.objects.create(name=name,salary=salary,email=email) #Employee.name=emp.n ,salary=s ,email=e  

        emp.save()
        print ("employee created")        
        return HttpResponse("Employee created")
    
    else:
        return render(request , "create.html")
    
'''''''''
def show(request):
    context={}   #empty dictionary
    emp=Employee.objects.all()  #get all the objects stored in emp
    for i in emp:
        print(i.name,i.salary,i.email)   #print the objects in console
        print(emp)
        return render(request,"dashboard.html")
        
'''''''''    

    
def dashboard(request):
    emp=Employee.objects.all() # Retrieve all Employee objects from the database
    context={'data':emp}    # Create a dictionary named context with key "data" and value emp
    return render(request,"dashboard.html",context) # Render the dashboard.html template with the context data

def delete(request,rid):
    emp=Employee.objects.all()
    context={'data':emp}
    delete_employee=Employee.objects.filter(id=rid) # Retrieve the Employee object to be deleted based on the provided id
    delete_employee.delete()
    return render(request,"dashboard.html",context)

def edit(request,rid):
    if request.method =="GET":
        emp=Employee.objects.filter(id=rid)
        context={'data':emp}
        return render(request,"edit.html",context)
     
    elif request.method=="POST":
        name=request.POST["name"]      #n
        salary=request.POST["salary"]  #s
        email=request.POST["email"]    #e
        
        edit_employee=Employee.objects.filter(id=rid).update(name=name,salary=salary,email=email)
        return redirect("index.html")


def  base(request):
    return render(request,"base.html")




        
        
        
        
    

        
        
    