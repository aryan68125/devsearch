# all the model forms generated by django will be defined here for this projects application for this django project
from django.forms import ModelForm
from . models import Project

#to create a model from I am going to create a simple class here
class ProjectForm(ModelForm):
    # at a minimum the model form is gonna require two fields 1. a model that we are gonna create a from for and
    class Meta:
        model = Project
        fields = ['title', 'discription', 'demo_link', 'source_link', 'tags', 'featured_image',]