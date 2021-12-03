from django import forms
from .models import Residents, Properties, STATUS_CHOICES, PROPERTY_TYPES


class NewResidentForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': " Residents First Name"
            }
        ))

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Resident's Last Name"
            }
        ))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Resident's Email Address"
            }
        ))

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-select',
                'placeholder': 'Occupancy Status'
            }
        ))

    class meta:
        model = Residents
        fields = ('house', 'first_name', 'last_name', 'email', 'status')


class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search',
                'class': 'form-control'
            }
        ))

    class meta:
        fields = 'search'


class ResidentInfoForm(forms.ModelForm):
    resident_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "readonly": True
            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "readonly": True
            }
        ))

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "readonly": True
            }
        ))

    resident_email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                "readonly": True
            }
        ))

    mobile_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "readonly": True
            }
        ))

    occupancy_start = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'id': 'datetimepicker12',
                "readonly": True
            }
        ))
    occupancy_status = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                "readonly": True
            }
        ))

    class Meta:
        model = Residents
        fields = ('resident_code', 'house', 'first_name', 'last_name', 'resident_email',
                  'mobile_number', 'occupancy_start', 'occupancy_status')


class ResidentUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ))

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ))

    resident_email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        ))

    mobile_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ))

    occupancy_start = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'id': 'datetimepicker12',
            }
        ))

    class Meta:
        model = Residents
        fields = ('resident_code', 'house', 'first_name', 'last_name', 'resident_email',
                  'mobile_number', 'occupancy_start')


class NewPropertyForm(forms.Form):
    prop_type = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control form-select'
            }
        ),
        choices=PROPERTY_TYPES
    )

    prop_desc = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Properties
        fields = ('prop_type', 'prop_desc')


class EditPropertyForm(forms.ModelForm):
    property_type = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control form-select'
            }
        ),
        choices=PROPERTY_TYPES
    )

    property_desc = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Properties
        fields = ('property_type', 'property_desc', 'property_code')
