from django.urls import path, include
from . import views

urlpatterns = [
    path('adm/', include(([
        path('dashboard/', views.admin_index, name="dashboard"),
    ], 'kgera'), namespace='my_admin')),

    path('', views.landing, name="landing"),
]
