from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('',views.home,name=""),
    # path('research',views.research,name="research"),
    # path('project',views.project,name="project"),
    # path('skill',views.skill,name="skill"),
    # path('course',views.course,name="course"),
    # path('award',views.award,name="award"),
    # path('switch',views.switch,name="switch"),
    # path('project/Audio8D', views.Audio8D,name='Audio8D'),
]