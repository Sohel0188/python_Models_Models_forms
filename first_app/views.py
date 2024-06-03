from django.shortcuts import render,redirect
from . import models,forms
def Home(request):
    student = models.Student.objects.all()
    print(student)
    return render(request,'first_app/home.html',{'data':student})

def delete(request,roll):
    data = models.Student.objects.get(pk = roll).delete()
    return redirect('home')

def add_teacher(request):
    if request.method == 'POST':
        form = forms.TeacherForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.TeacherForm()
    return render(request,'first_app/add_teachers.html',{'form':form})
    