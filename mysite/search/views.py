from search.forms import DestinationForm, SearchForm, PointOfInterestForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from search.models import Destination, AttractionCategory
from pygeocoder import Geocoder
from gmapi import maps
from gmapi.forms.widgets import GoogleMap
from django.http import HttpResponse
import json

def index(request):
    context = RequestContext(request)
    gmap = maps.Map(opts = {
        'mapTypeId': maps.MapTypeId.ROADMAP,
        'zoom': 7,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
    })
    
    converted=""
    if request.method == 'POST':
        form = SearchForm(request.POST)
        
        if form.is_valid():
            new_obj = Destination()
            new_obj.category_id = 1
            searchlocation = form.cleaned_data['searchfor']
            geoloc = Geocoder.geocode(searchlocation)[0]
            converted = str(geoloc)
            print(converted)
            lat, lng = geoloc.coordinates
            marker = maps.Marker(opts = {
                'map': gmap,
                'position': maps.LatLng(lat, lng),
            })
            maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
            maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
            info = maps.InfoWindow({
                'content': 'Hello!',
                'disableAutoPan': True
            })
            info.open(gmap, marker)
            #new_obj.save();
            form = SearchForm()
        else:
            print form.errors
    else:
        form = SearchForm()

    dict = {'form': SearchForm(initial={'map': gmap}), 'converted': converted}
    return render_to_response('search/index.html', dict, context);

def add_destination(request):
    context = RequestContext(request)
 
    converted=""
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        
        if form.is_valid():
            #new_obj = Destination()
            searchlocation = form.cleaned_data['searchfor']
            geoloc = Geocoder.geocode(searchlocation)[0]
            converted = str(geoloc)
            #new_obj.save();
        else:
            print form.errors
        return HttpResponse(json.dumps({'message': converted}), mimetype='application/json')
    else:
        form = DestinationForm()

    dict = {'form': form, 'converted': converted}
    return render_to_response('search/add_destination.html', dict, context);

def add_point_of_interest(request):
    context = RequestContext(request)
    if request.method == "POST":
        form = PointOfInterestForm(request.POST)
        if form.is_valid():
            print 'going to save'
            print form.cleaned_data['name']
            form.save()
            print 'saved'
        else:
            print form.errors
    else:
        form = PointOfInterestForm()
    return render_to_response('search/add_point_of_interest.html', {'form': form}, context)

def search_for_location(request):
    # To handle AJAX requests from the form
    if request.method == "POST":
        searchlocation = request.POST['searchfor']
        geoloc = Geocoder.geocode(searchlocation)[0]
        # TODO: Do something if we can't find the place
        return HttpResponse(json.dumps({'message': str(geoloc)}))
