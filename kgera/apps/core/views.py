from django.db.models.aggregates import Count
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..core.decorators import admin_required

from django.utils.decorators import method_decorator
from .decorators import admin_required, basic_required
from django.template import loader
from django.http import HttpResponseRedirect


# noinspection PyUnresolvedReferences
from ..structure.models import Houses, HouseType, Community, CommunityType
from ..residents.models import Residents, Properties, CommunityHeads


@login_required()
@admin_required()
def admin_index(request):
    # Structure Counter
    all_commtype = CommunityType.objects.all()
    all_communities = Community.objects.all()
    all_housetype = HouseType.objects.all()
    all_houses = Houses.objects.all()
    house_count = all_houses.count()
    commtype_count = all_commtype.count()
    communities_count = all_communities.count()
    housetype_count = all_housetype.count()

    # Residents Counter
    activeresidents = Residents.objects.filter(occupancy_status=1)
    vacatedresidents = Residents.objects.filter(occupancy_status=0)
    communityheads = CommunityHeads.objects.filter(appointment_status=1)
    properties = Properties.objects.all()

    # Get Data Count
    activeresidents_count = activeresidents.count()
    vacatedresidents_count = vacatedresidents.count()
    activecommunity_heads = communityheads.count()
    property_count = properties.count()

    context = {
        'housetype_count': housetype_count,
        'commtype_count': commtype_count,
        'communities_count': communities_count,
        'house_count': house_count,
        'activeresidents_count': activeresidents_count,
        'vacatedresidents_count': vacatedresidents_count,
        'activecommunity_heads': activecommunity_heads,
        'property_count': property_count,
    }
    return render(request, "dashboards/index.html", context)


def landing(request):
    return HttpResponseRedirect("https://kgera.org.ng/")

