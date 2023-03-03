from django.urls import path

import objects.views as views

urlpatterns = [
    path('objects/', views.ObjectList.as_view())
]