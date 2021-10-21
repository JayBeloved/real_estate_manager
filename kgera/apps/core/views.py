from django.db.models.aggregates import Count
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from django import template


from kgera.apps.structure.models import Houses, HouseType, Community, CommunityType


@login_required(login_url="/login/")
def index(request):
    all_commtype = CommunityType.objects.all()
    all_communities = Community.objects.all()
    all_housetype = HouseType.objects.all()
    all_houses = Houses.objects.all()
    house_count = all_houses.count()
    commtype_count = all_commtype.count()
    communities_count = all_communities.count()
    housetype_count = all_housetype.count()

    context = {
        'housetype_count': housetype_count,
        'commtype_count' : commtype_count,
        'communities_count' : communities_count,
        'house_count' : house_count
    }
    return render(request,"dashboards/index.html", context)