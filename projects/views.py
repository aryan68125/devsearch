from django.shortcuts import render, redirect

from django.http import HttpResponse

from . models import Project

#now indorder to use a model form that we jsut created in the forms.py we are just gonna import it into our views.py
from .forms import ProjectForm

# Create your views here.

def projects(request):
    projects = Project.objects.all()
    data_for_front_end = {
        'projects' : projects,
    }
    return render(request, 'projects/projects_list.html', data_for_front_end)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()

    data_for_front_end = {
        'projectObj':projectObj,
        'tags':tags,
    }
    return render(request, 'projects/single-project.html', data_for_front_end)

#this view function will create a model form for us for creating a project in the project app in django
def createProject(request):
    # here we will create a form that will be generated by the model form in the forms.py file by the class ProjectForm
    form = ProjectForm()

    if request.method == 'POST':
        #for debugging
        print(request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid(): #save the form data if the form is valid and it will add the newly created object to the database
            form.save()
            return redirect('projects')

    data_for_front_end = {
         'form':form,
    }
    return render(request, "projects/project_form.html", data_for_front_end)

#create an update view and here we are gonna reuse the model form from form.py file that we created inside our projects application in our django project
def updateProject(request, pk):
    project = Project.objects.get(id=pk) #here we are gonna get the project from the database that has the id matching to the primary key that is passed from the front end
    # here we will create a form that will be generated by the model form in the forms.py file by the class ProjectForm
    form = ProjectForm(instance = project) #the only difference between createView and updateView is we are gonna pass in an instance
                         #so an instance is gonna be the project that we are gonna edit

    if request.method == 'POST':
        #for debugging
        print(request.POST)
        form = ProjectForm(request.POST , instance = project) # here pass request.POST along with what project are we updating at the moment instance = project
        if form.is_valid(): #save the form data if the form is valid and it will add the newly created object to the database
            form.save()
            return redirect('projects')

    data_for_front_end = {
         'form':form,
    }
    return render(request, "projects/project_form.html", data_for_front_end)

#create a function for deleting a project in the projects application of this django project
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete() #delete the project from the database
        return redirect('projects')
    data_for_front_end ={
        'object':project,
    }
    return render(request, "projects/delete_template.html", data_for_front_end)
