from django.urls import path, include

from . import views

from .views import select_house

urlpatterns = [
    path('new_account/', include(([
        path('select_house/', select_house.as_view(), name="select_house"),
        path('account_request/house<int:house_id>/', views.account_request, name="account_request"),
    ], 'kgera'), namespace="new_account")),

    path('resident/', include(([
            path('dashboard/', views.resident_dashboard, name="resident_dashboard"),
            path('update/primary_details/', views.update_info, name="update_info"),
            path('properties/property<int:property_id>/edit', views.edit_property,
                 name="edit_property"),
        ], 'kgera'), namespace="resident_account")),

    path('user/', include(([
            path('profile/', views.profile, name="profile"),
            path('update/profile_picture', views.profile_pics, name="profile_picture"),
            path('update/profile_info/', views.profile_info, name="profile_info"),
            path('update/password_reset/', views.profile_password, name="password_reset"),
        ], 'kgera'), namespace='resident_profile')),
    ]

