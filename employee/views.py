from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Employee
from django.views.generic import View

# Create your views here.

class EmployeeView(ListView):
    model = Employee
    template_name = 'employee/emp.html'
    context_object_name = 'employees'



class CreateEmployee(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        roll_no1 = request.GET.get('rollno', None)
        class_name1 = request.GET.get('classname', None)
        print('name', name1)
        print('roll_no', roll_no1)
        print('class_name1', class_name1)

        obj, created = Employee.objects.get_or_create(
            name = name1,
            roll_no = roll_no1,
            class_name = class_name1
        )

        user = {'id':obj.id,'name':obj.name,'roll_no':obj.roll_no,'class_name':obj.class_name}

        data = {
            'user': user
        }
        return JsonResponse(data)


class UpdateEmployee(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        roll_no1 = request.GET.get('rollno', None)
        class_name1 = request.GET.get('classname', None)

        obj = Employee.objects.get(id=id1)
        obj.name = name1
        obj.roll_no = roll_no1
        obj.class_name = class_name1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'roll_no':obj.roll_no,'class_name':obj.class_name}

        data = {
            'user': user
        }
        return JsonResponse(data)


class DeleteEmployee(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Employee.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)