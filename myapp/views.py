from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics          
from .serializers import EmployeeSerializer     
from .models import Employee 
from .pagination import CustomPagination                
        
class EmployeeRUDView(generics.RetrieveUpdateDestroyAPIView):       
    serializer_class = EmployeeSerializer

    def get_queryset(self, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            content = {
                'message': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        
        return employee

    # get an employee HTTP GET
    def get(self, request, pk):
        employee = self.get_queryset(pk)
        serializer = EmployeeSerializer(employee)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # update an employee HTTP PUT
    def put(self, request, pk):        
        employee = self.get_queryset(pk)
        serializer = EmployeeSerializer(employee, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete an employee HTTP DELETE
    def delete(self, request, pk):
        employee = self.get_queryset(pk)
        employee.delete()
        content = {
            'message': 'data was deleted'
        }
        
        return Response(content, status=status.HTTP_204_NO_CONTENT)


class EmployeeView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer    
    pagination_class = CustomPagination

    def get_queryset(self):
       employees = Employee.objects.all()

       return employees

    # get all employees
    def get(self, request):
        employees = self.get_queryset()

        # serializer = self.serializer_class(employees, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

        # pagination
        paginate_queryset = self.paginate_queryset(employees)
        serializer = self.serializer_class(paginate_queryset, many=True)    
        return self.get_paginated_response(serializer.data)

    # create a new employee
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)