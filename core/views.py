from django.shortcuts import render,reverse
from .forms import StudentRegistration
from .models import Student
from django.http import HttpResponseRedirect


def home(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pwrd=fm.cleaned_data['password']
            print('Form Validated')
            print('name:',nm)
            print('email:',em)
            print('password:',pwrd)
            student=Student(name=nm,email=em,password=pwrd)
            student.save()
    else:
        fm=StudentRegistration()
    students=Student.objects.all()
    return render(request,'core/home.html',{'form':fm, 'students':students})



def edit(request,id):
    student=Student.objects.get(pk=id)
    if request.method=="POST":
        fm=StudentRegistration(request.POST,instance=student)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        fm=StudentRegistration(instance=student)
    return render(request,'core/edit.html',{'form':fm})

def delete(request,id):
    student=Student.objects.get(pk=id)
    student.delete()
    return HttpResponseRedirect(reverse('home'))