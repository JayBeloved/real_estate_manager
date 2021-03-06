from django.urls import path, include

from . import views
from .views import all_service_charge, all_transformer_levy
urlpatterns = [
    path('financials/', include(([
        path('resident<int:resident_id>/dashboard/', views.financials_dashboard, name="financials_dashboard"),
        path('service_charge/all/', all_service_charge.as_view(), name='all_service_charge'),
        path('transformer_levy/all/', all_transformer_levy.as_view(), name='all_transformer_levy'),
    ], 'kgera'), namespace='financials')),
]
