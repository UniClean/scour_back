from django.urls import path

import orders.views as views

urlpatterns = [
    path('orders/', views.OrderList.as_view())
]