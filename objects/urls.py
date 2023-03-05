from django.urls import path

import objects.views as views

urlpatterns = [
    path('objects/', views.ObjectList.as_view()),
    path('objects/<int:id>/', views.ObjectDetail.as_view(), name='object-retrieve'),
    path('objects/<int:id>/update/', views.ObjectUpdate.as_view(), name='object-update'),
    path('objects/<int:id>/delete/', views.ObjectDestroy.as_view(), name='object-destroy'),
]