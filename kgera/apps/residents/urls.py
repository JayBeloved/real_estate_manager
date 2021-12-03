from django.urls import path, include
from . import views
from .views import select_house, all_residents, select_request

urlpatterns = [
    path('residents/', include(([
        path('', views.residents_dashboard, name="residents_dashboard"),
        path('select_house/', select_house.as_view(), name="select_house"),
        path('select_request/', select_request.as_view(), name="select_request"),
        path('cancel_request/<int:pk>/', views.cancel_account_request, name="cancel_request"),
        path('house<int:house_id>/new_resident/', views.newresident_dashboard, name="newresident_dashboard"),
        path('request<int:request_id>/house<int:house_id>/new_resident/', views.new_resident_request,
             name="new_resident_request"),
        path('all/', all_residents.as_view(), name="all_residents"),
        path('resident<int:resident_id>/details/', views.residents_info, name="resident_details"),
        path('resident<int:resident_id>/details/update', views.update_resident_info, name="resident_details_update"),
        path('resident<int:resident_id>/property<int:property_id>/edit', views.edit_property,
             name="resident_property_edit"),
        ], 'kgera'), namespace='residents')),
]
