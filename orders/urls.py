from django.urls import path

import orders.views as views

urlpatterns = [
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:id>/', views.OrderDetailView.as_view(), name='order_detail'),
]