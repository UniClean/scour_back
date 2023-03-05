from django.urls import path

import customers.views as views

urlpatterns = [
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:id>/', views.CustomerDetail.as_view(), name='customer-retrieve'),
    path('customers/<int:id>/update/', views.CustomerUpdate.as_view(), name='customer-update'),
    path('customers/<int:id>/delete/', views.CustomerDestroy.as_view(), name='customer-destroy'),
]