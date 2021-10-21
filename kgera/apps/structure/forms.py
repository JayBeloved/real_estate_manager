from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Houses, HouseType, Community, CommunityType

# Count Choices
NONE = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10

COUNT_CHOICES = (
    (NONE, ('None')),
    (ONE, ('One')),
    (TWO, ('Two')),
    (THREE, ('Three')),
    (FOUR, ('Four')),
    (FIVE, ('Five')),
    (SIX, ('Six')),
    (SEVEN, ('Seven')),
    (EIGHT, ('Eight')),
    (NINE, ('Nine')),
    (TEN, ('Ten')),
)



# True/False Choices

YES = True
NO = False

BOOL_CHOICES = (
    (YES, ("Yes It Has")),
    (NO, ("No It Doesn't"))
)

BOOL_CHOICES2 = (
    (YES, ("Yes, Proceed")),
    (NO, ("No, Cancel"))
)

#House Type Creation Form
class HousetypeCreationForm(forms.Form):
    htype = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control'
            }
        )
    )
        
    is_block = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class' : 'form-control form-select'
            },
        ),
        choices=BOOL_CHOICES
    )

    block_count = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(
            attrs={
                'class' : 'form-control form-select'
            }
        )
    )
    is_flat = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class' : 'form-control form-select'
            },
        ),
        choices=BOOL_CHOICES
    )


    flat_count = forms.ChoiceField(
        choices=COUNT_CHOICES,
        widget=forms.Select(
            attrs={
                'class' : 'form-control form-select'
            }
        )
    )

    class meta:
        model = HouseType
        fields = ('htype', 'is_block', 'block_count', 'is_flat', 'flat_count')

###########################################################

# CommunityType Creation Form
class CommunityTypeCreationForm(forms.Form):
    housetype = forms.ModelChoiceField(
        HouseType.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control form-select'
            }
        )
    )
    commtype = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control'
            }
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control'
            }
        )
    )

    class meta:
        model = CommunityType
        fields = ('housetype', 'commtype', 'description')

###########################################################

# Community Creation Form
class CommunityCreationForm(forms.Form):
    communitytype = forms.ModelChoiceField(
        CommunityType.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control form-select'
            }
        )
    )
    commnum = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class' : 'form-control'
            }
        )
    )

    class meta:
        model = Community
        fields = ('housetype', 'commtype')

#House Type Approval Form
class HouseApprovalForm(forms.Form):
    approval=forms.ChoiceField(
        choices=BOOL_CHOICES2,
        widget=forms.Select(
            attrs={
                'class' : 'form-control form-select'
            }
        ))
    class meta:
        fields = ('approval')