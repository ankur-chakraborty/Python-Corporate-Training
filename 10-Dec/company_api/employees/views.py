from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
import json


@csrf_exempt
def employees_api(request):
    if request.method == 'GET':
        employees = list(Employee.objects.values())
        return JsonResponse(employees, safe=False)

    if request.method == 'POST':
        body = json.loads(request.body)
        emp = Employee.objects.create(
            name=body['name'],
            role=body['role'],
            salary=body['salary']
        )
        return JsonResponse({"message": "Employee created", "id": emp.id})


@csrf_exempt
def employee_api(request, id):
    try:
        emp = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)

    if request.method == 'GET':
        return JsonResponse({
            "id": emp.id,
            "name": emp.name,
            "role": emp.role,
            "salary": emp.salary
        })

    if request.method == 'PUT':
        body = json.loads(request.body)
        emp.name = body.get('name', emp.name)
        emp.role = body.get('role', emp.role)
        emp.salary = body.get('salary', emp.salary)
        emp.save()
        return JsonResponse({"message": "Employee updated"})

    if request.method == 'DELETE':
        emp.delete()
        return JsonResponse({"message": "Employee deleted"})