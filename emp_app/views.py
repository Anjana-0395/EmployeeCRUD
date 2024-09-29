from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])

def employee(request):
    if request.method == 'GET':
        objEmployee = Employee.objects.all()
        serializer = EmployeeSerializer(objEmployee, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = EmployeeSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'PUT':
        data = request.data
        try:
            obj = Employee.objects.get(id=data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)
        
        serializer = EmployeeSerializer(obj, data=data, partial=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'PATCH':
        data = request.data
        try:
            obj = Employee.objects.get(id=data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)
        
        serializer = EmployeeSerializer(obj, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        data = request.data
        try:
            obj = Employee.objects.get(id=data['id'])
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)
        
        obj.delete()
        return Response({"message": "Person deleted succesfully"}, status=204)
    





from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    



@api_view(['GET'])
def index(request):
    employee_details = {
        "name" : "Anu",
        "designation" : "Accountant",
        "age" : 30,
        "location" : "Thrissur"
    }
    return Response(employee_details)