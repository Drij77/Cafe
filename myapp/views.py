from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from .forms import AddressForm,CafeForm,EditCafeForm
from .models import Address, Cafe, Country, State, City, Area, SubArea
from django.core.paginator import Paginator


def create_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('address_list')
    else:
        form = AddressForm()
    return render(request, 'add_address.html', {'form': form})

def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'address_list.html', {'addresses': addresses})

def create_location(request):
    if request.method == 'POST':
        form = CafeForm(request.POST)
        if form.is_valid():
            location = form.save()
            return ('Done Successfully')
    else:
        form = CafeForm()
    return render(request, 'create_location.html', {'form': form})


def search_cafes(request):
    cafes = Cafe.objects.all()
    countries = Country.objects.all()
    states = State.objects.all()
    cities = City.objects.all()
    areas = Area.objects.all()
    subareas = SubArea.objects.all()

    if 'country' in request.GET:
        country = request.GET['country']
        if country:
            cafes = cafes.filter(address__area__city__state__country__name=country)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            cafes = cafes.filter(address__area__city__state__name=state)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cafes = cafes.filter(address__area__city__name=city)

    if 'area' in request.GET:
        area = request.GET['area']
        if area:
            cafes = cafes.filter(address__area__name=area)

    if 'subarea' in request.GET:
        subarea = request.GET['subarea']
        if subarea:
            cafes = cafes.filter(address__name=subarea)

    paginator = Paginator(cafes, 5)
    page_number = request.GET.get('page')
    cafes = paginator.get_page(page_number)

    context = {
        'cafes': cafes,
        'countries': countries,
        'states': states,
        'cities': cities,
        'areas': areas,
        'subareas': subareas,
    }

    return render(request, 'search_cafes.html', context)


def delete_cafe(request, cafe_id):
    cafe = get_object_or_404(Cafe, id=cafe_id)
    if request.method == 'POST':
        cafe.delete()
        return JsonResponse({'success': True})
    context = {
        'cafe': cafe,
    }
    html = render_to_string('delete_cafe.html', context, request=request)
    return JsonResponse({'html': html})





def edit_cafe(request, cafe_id):
    cafe = get_object_or_404(Cafe, id=cafe_id)
    form = EditCafeForm(request.POST or None, instance=cafe)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True})
    context = {
        'form': form,
        'cafe': cafe,
    }
    return render(request, 'edit_cafe.html', context)