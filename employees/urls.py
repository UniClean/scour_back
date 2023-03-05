from django.urls import path

import employees.views as views

urlpatterns = [
    path('employees/', views.EmployeeList.as_view()),
    path('position/', views.PositionList.as_view()),
]