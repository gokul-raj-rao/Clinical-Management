"""aclinicals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from clinicalsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view/',views.PatientListView.as_view(),name='index'),
    path('view/create/',views.PatientCreateView.as_view()),
    path('view/update/<int:pk>/',views.PatientUpdateView.as_view()),
    path('view/delete/<int:pk>/',views.PatientDeleteView.as_view()),
    path('view/addData/<int:pk>/',views.addData),
    path('view/analyze/<int:pk>/',views.analyze),
    path('',views.home,name="home"),
    path('login/',views.LoginPage,name='login'),
    
    path('logout/',views.LogoutPage,name='logout'),
    path('view/select/', views.select_date, name='select_date'),
    path('view/all/',views.pa,name="all"),
    path('view/all/delete/<int:post_id>/',views.delete_appointment,name="all_del"),
]
