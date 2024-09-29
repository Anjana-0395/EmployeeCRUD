from django.contrib import admin
from django.urls import path,include
from emp_app.views import employee,index


from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)



urlpatterns = [
    path('details/', index),
    path('employee/', employee, name='employee'),

    
    
]+router.urls