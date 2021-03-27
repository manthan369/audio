"""audio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('file_create', views.AudioCreate.as_view(), name='audio_list'),
    path('delete/<int:pk>/', views.AudioDelete.as_view(), name='audio_list'),
    path('edit/<int:pk>/', views.AudioUpdate.as_view(), name='audio_list'),
    path('add/<int:pk>', views.AudioList.as_view(), name='audio_list'),
]
