from django import forms
from search.models import Destination, Attraction, AttractionCategory
from gmapi import maps
from gmapi.forms.widgets import GoogleMap
from datetime import datetime 
from pygeocoder import Geocoder

class SearchForm(forms.Form):
	searchfor = forms.CharField(max_length=50, help_text="Please enter the destination name")
	map = forms.Field(widget=GoogleMap(attrs={'width':500, 'height':500}), required=False)
    #name = forms.CharField(max_length=50, help_text="Please enter the destination name")
    #state = forms.CharField(max_length=50, help_text="State name")
    #country = forms.CharField(max_length=50, help_text="Country name")
    #address = forms.CharField(max_length=50)
    #location = forms.CharField(max_length=30)
    #category_id = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    #description = forms.CharField(max_length=200)
    #best_time = forms.CharField(max_length=50)
    #open_hours = forms.CharField(max_length=50)
    #time_required = forms.CharField(max_length=50)
    #photos = forms.CharField(max_length=50)
    #added_on = forms.DateField()
    #added_by = forms.CharField(max_length=20)

    #def clean(self):
    #   cleaned_data = self.cleaned_data
    #    print(cleaned_data)
    #    cleaned_data['category_id'] = 2
    #    return cleaned_data

    #class Meta:
        #model = Destination
        #fields = ('name', 'state', 'country', 'address', 'location', 'description', 'best_time', 'open_hours', 'time_required', 'photos', 'added_on', 'added_by')

class DestinationForm(forms.Form):
	searchfor = forms.CharField(max_length=50, help_text="Please enter the destination name:")

class PointOfInterestForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.HiddenInput(), required=False)
    state = forms.CharField(max_length=50, widget=forms.HiddenInput(), required=False)
    country = forms.CharField(max_length=50, widget=forms.HiddenInput(), required=False)
    address = forms.CharField(max_length=50,
                              widget=forms.TextInput(attrs={'size':80,'readonly':'readonly'}),
                              help_text="Address",
                              required=False)
    location = forms.CharField(max_length=30, widget=forms.HiddenInput(), required=False)

    category = forms.ModelChoiceField(queryset=AttractionCategory.objects.all(), help_text="Choose category", required=False, initial=1, empty_label=None)
    description = forms.CharField(max_length=200, help_text="Add description", required=False)
    best_time = forms.CharField(max_length=50, help_text="Best time to visit", required=False)
    open_hours = forms.CharField(max_length=50, help_text="Open hours", required=False)
    ticket_price = forms.CharField(max_length=50, help_text="Ticket price", required=False)
    time_required = forms.CharField(max_length=50, help_text="Time required", required=False)

    photos = forms.CharField(max_length=50, widget=forms.HiddenInput(), required=False)
    added_on = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    added_by = forms.CharField(max_length=20, widget=forms.HiddenInput(), required=False);

    def clean(self):
        cleaned_data = self.cleaned_data
        searchlocation = cleaned_data['address']
        geoloc = Geocoder.geocode(searchlocation)[0]
        cleaned_data['name'] = str(geoloc).split(',')[0].strip()
        cleaned_data['state'] = geoloc.state
        cleaned_data['country'] = geoloc.country
        cleaned_data['location'] = str(geoloc.coordinates)
        cleaned_data['added_by'] = "aju"
        #I'm wondering why this is not handled by the the default value tha tis being set. Enough time wasted on this.
        cleaned_data['added_on'] = datetime.utcnow()
        print(cleaned_data)
        return cleaned_data

    class Meta:
        model = Attraction
        fields = ['name', 'state', 'country', 'address', 'location', 'category', 'description', 'best_time',
                  'open_hours', 'ticket_price', 'time_required', 'photos', 'added_on', 'added_by']


