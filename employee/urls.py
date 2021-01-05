from django.urls import path
from employee import  views 

urlpatterns = [
    path('',  views.EmployeeView.as_view(), name='employee'),
    path('createEmp', views.CreateEmployee.as_view(), name='create'),
    path('updateEmp', views.UpdateEmployee.as_view(), name='update'),
    path('deleteEmp', views.DeleteEmployee.as_view(), name='delete'),
]