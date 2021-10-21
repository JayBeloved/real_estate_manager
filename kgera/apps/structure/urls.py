from django.urls import path,include
from .views import HouseTypeListView, CommunityListView, CommunityTypeListView, HouseListView
from . import views

urlpatterns = [
    path('housetypes/', include(([
        path('', views.housetype_dashboard, name="housetype_dashboard"),
        path('all/', HouseTypeListView.as_view(), name="all_housetypes"),
    ], 'kgera'), namespace='housetype')),

    path('communitytypes/', include(([
        path('', views.commtype_dashboard, name="commtype_dashboard"),
        path('all/', CommunityTypeListView.as_view(), name="all_commtypes")
    ], 'kgera'), namespace='commtype')),
    
    path('communities/', include(([
        path('', views.communities_dashboard, name="communities_dashboard"),
        path('all/', CommunityListView.as_view(), name="all_communities")
    ], 'kgera'), namespace='communities')),

    path('houses/', include(([
        path('', views.houses_dashboard, name="houses_dashboard"),
        path('all/', HouseListView.as_view(), name="all_houses")
    ], 'kgera'), namespace='houses')),
]