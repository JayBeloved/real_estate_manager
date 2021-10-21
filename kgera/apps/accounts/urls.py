from django.urls import path, include
from django.contrib.auth.views import LogoutView as logout_view
from . import views

urlpatterns = [
    path('login/', views.login_view, name="login"),

    path('logout/', logout_view.as_view(), name="logout"),

    path('profile/', include(([
        path('', views.profile, name="profile"),
        path('profile_picture', views.profile_pics, name="profile_picture"),
        path('profile_info/', views.profile_info, name="profile_info"),
        path('password_reset/', views.profile_password, name="password_reset"),
    ], 'kgera'), namespace='profile')),
]
