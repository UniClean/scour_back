from django.urls import path

import customers.views as views

urlpatterns = [
    path('customers/', views.CustomerList.as_view())
]