from sqlite3 import IntegrityError

from django import forms
from .models import Address, Country, State, City, Area, SubArea

from .models import Cafe


class AddressForm(forms.ModelForm):
    country_name = forms.CharField(max_length=100)
    state_name = forms.CharField(max_length=100)
    city_name = forms.CharField(max_length=100)
    area_name = forms.CharField(max_length=100)
    sub_area_name = forms.CharField(max_length=100)

    class Meta:
        model = Address
        fields = ['country_name', 'state_name', 'city_name', 'area_name', 'sub_area_name']

    def save(self, commit=True):
        # Get or create the Country object
        country, created = Country.objects.get_or_create(name=self.cleaned_data['country_name'])

        # Get or create the State object
        state, created = State.objects.get_or_create(name=self.cleaned_data['state_name'], country=country)

        # Get or create the City object
        city, created = City.objects.get_or_create(name=self.cleaned_data['city_name'], state=state)

        # Get or create the Area object
        area, created = Area.objects.get_or_create(name=self.cleaned_data['area_name'], city=city)

        # Get or create the SubArea object
        sub_area, created = SubArea.objects.get_or_create(name=self.cleaned_data['sub_area_name'], area=area)

        # Create the Address object
        address = Address.objects.create(sub_area=sub_area)

        # Return the Address object
        return address


class CafeForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)

    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="-- Select Country --")
    state = forms.ModelChoiceField(queryset=State.objects.none(), empty_label="-- Select State --")
    city = forms.ModelChoiceField(queryset=City.objects.none(), empty_label="-- Select City --")
    area = forms.ModelChoiceField(queryset=Area.objects.none(), empty_label="-- Select Area --")
    subarea = forms.ModelChoiceField(queryset=SubArea.objects.none(), empty_label="-- Select SubArea --")

    class Meta:
        model = Cafe
        fields = ['name', 'address']


    def save(self, commit=True):
        # Get the Location object from the form's instance variable
        instance = super(CafeForm, self).save(commit=False)

        # Set the latitude and longitude fields from the form's cleaned data
        instance.latitude = self.cleaned_data['latitude']
        instance.longitude = self.cleaned_data['longitude']

        # If commit is True, save the instance to the database
        if commit:
            instance.save()

        # Return the Location object
        return instance


class EditCafeForm(forms.ModelForm):
    pass
