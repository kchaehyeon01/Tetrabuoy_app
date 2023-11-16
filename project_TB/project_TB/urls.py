"""
URL configuration for project_TB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app_tetrabuoy import views as views_tetrabuoy
from app_tetline import views as views_tetline
from app_data import views as views_data
from app_settings import views as views_settings

urlpatterns = [
    path("admin/", admin.site.urls),

    # views_tetrabuoy
    path("start", views_tetrabuoy.start, name = "start"),
    path("tetrabuoy_map", views_tetrabuoy.tetrabuoy_map, name="tetrabuoy_map"),
    path("tetrabuoy_list", views_tetrabuoy.tetrabuoy_list, name="tetrabuoy_list"),
    path("tetrabuoy_add", views_tetrabuoy.tetrabuoy_add, name="tetrabuoy_add"),
    path("tetrabuoy_detail/<int:buoy_id>", views_tetrabuoy.tetrabuoy_detail, name = "tetrabuoy_detail"),
    path("tetrabuoy_edit/<int:buoy_id>", views_tetrabuoy.tetrabuoy_edit, name = "tetrabuoy_edit"),
    path("tetrabuoy_delete/<int:buoy_id>", views_tetrabuoy.tetrabuoy_delete, name="tetrabuoy_delete"),
    
    # views_tetline
    path("tetline_map", views_tetline.tetline_map, name="tetline_map"),
    path('tetline_list', views_tetline.tetline_list, name="tetline_list"),
    path("tetline_add", views_tetline.tetline_add, name="tetline_add"),
    path('tetline_detail/<int:line_id>', views_tetline.tetline_detail, name='tetline_detail'),
    
    # views_data
    path('data_main', views_data.data_main, name = "data_main"),
    
    # views_settings
    path('settings_main', views_settings.settings_main, name = "settings_main"),
    path('settings_init', views_settings.settings_init, name="settings_init"),
]
