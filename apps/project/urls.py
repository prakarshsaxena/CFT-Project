from django.urls import path
from django.views.generic import TemplateView
from . import views

from .views import ProjectList, Employee_Project_List, ProjectCreate, Edit_Project, Details_Project
app_name = 'project'


urlpatterns = [
    path('', ProjectList.as_view(template_name="project_manager_view.html"), name="manager-project-view"),
    path('add/', ProjectCreate.as_view(), name='project-add'),
    path('employee/', Employee_Project_List.as_view(template_name="employee_view.html"), name="employee-project"),
    path('update/<int:pk>/', Edit_Project.as_view(), name='project-update'),
    path('details/<int:pk>/', Details_Project.as_view(), name="project-details"),

]