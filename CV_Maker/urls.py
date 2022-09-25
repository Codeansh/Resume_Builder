"""CV_Maker URL Configuration

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
from django.urls import path, include

from cvm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_cv/', views.create_resume, name="create-resume"),
    path('<int:id>/', views.print_resume, name="print-resume"),
    path("register/", views.register, name="register"),
    path("", include("django.contrib.auth.urls")),
    path("", views.user_resume, name="user-resume"),
    path("cvview/<int:id>/", views.view_resume, name="view-resume"),
    path("cvdelete/<int:id>/", views.delete_resume, name="delete-resume"),
    path("cvupdate/<int:id>/", views.update_resume, name="update-resume"),
]
