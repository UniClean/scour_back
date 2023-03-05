from django.urls import path

import orders.views as views

urlpatterns = [
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:id>/', views.OrderDetail.as_view(), name='order_detail'),
    path('orders/<int:id>/update/', views.OrderUpdate.as_view(), name='order-update'),
    path('orders/<int:id>/delete/', views.OrderDestroy.as_view(), name='order-destroy'),
]