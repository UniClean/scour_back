from django.urls import path

import customers.views as views

urlpatterns = [
    path('customer/', views.CustomerList.as_view())
]