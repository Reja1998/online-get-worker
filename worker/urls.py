from django.urls import path
from .import views

urlpatterns=[
    path('',views.home, name='home'),
    path('project/<str:pk>/',views.project, name='project'),
    path('about/',views.About, name = 'about'),
    path('create-project',views.createProject,name='create-project'),
    path('update-project/<str:pk>/',views.updateProject,name='update-project'),
    path('delete-project/<str:pk>/',views.deleteProject,name='delete-project'),
    
]
