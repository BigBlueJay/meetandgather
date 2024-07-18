"""
Use views.py To Render Html Pages
"""

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

"""
Take in Request (Django sends request)
Retuen Html as a Response (We pick to return the response)
"""
def home_view(request):
    HTML_STRING = render_to_string("pages/home.html")
    return HttpResponse (HTML_STRING)

def bookings_view(request):
    HTML_STRING = render_to_string("pages/bookings.html")
    return HttpResponse (HTML_STRING)

def booking_request_view(request):
    HTML_STRING = render_to_string("pages/bookings-request-from.html")
    return HttpResponse (HTML_STRING)

def openhouse_view(request):
    HTML_STRING = render_to_string("pages/openhouse.html")
    return HttpResponse (HTML_STRING)

def events_view(request):
    HTML_STRING = render_to_string("pages/events.html")
    return HttpResponse (HTML_STRING)

def gallery_view(request):
    HTML_STRING = render_to_string("pages/gallery.html")
    return HttpResponse (HTML_STRING)

def contact_view(request):
    HTML_STRING = render_to_string("pages/contact.html")
    return HttpResponse (HTML_STRING)

def about_view(request):
    HTML_STRING = render_to_string("pages/about.html")
    return HttpResponse (HTML_STRING)

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def handler400(request, exception):
    return render(request, '400.html', status=400)

#def handler403(request):
    #return render(request, '403.html', status=403)
    
def page_not_found_view_403(request, exception):
    return render(request, '403.html', status=403)

#Alt Homepages
def home_view_gso(request):
    HTML_STRING = render_to_string("pages/home_gso.html")
    return HttpResponse (HTML_STRING)

def home_view_hp(request):
    HTML_STRING = render_to_string("pages/home_hp.html")
    return HttpResponse (HTML_STRING)

def home_view_ws(request):
    HTML_STRING = render_to_string("pages/home_ws.html")
    return HttpResponse (HTML_STRING)

#Alt Sell With Us Pages
def sell_with_us_view_gso(request):
    HTML_STRING = render_to_string("pages/sell_with_us_gso.html")
    return HttpResponse (HTML_STRING)

def sell_with_us_view_hp(request):
    HTML_STRING = render_to_string("pages/sell_with_us_hp.html")
    return HttpResponse (HTML_STRING)

def sell_with_us_view_ws(request):
    HTML_STRING = render_to_string("pages/sell_with_us_ws.html")
    return HttpResponse (HTML_STRING)

#Alt Steps to Sell Pages
def steps_view_gso(request):
    HTML_STRING = render_to_string("pages/steps_gso.html")
    return HttpResponse (HTML_STRING)

def steps_view_hp(request):
    HTML_STRING = render_to_string("pages/steps_hp.html")
    return HttpResponse (HTML_STRING)

def steps_view_ws(request):
    HTML_STRING = render_to_string("pages/steps_ws.html")
    return HttpResponse (HTML_STRING)

#Alt Contact Pages
def contact_us_view_gso(request):
    HTML_STRING = render_to_string("pages/contact_gso.html")
    return HttpResponse (HTML_STRING)

def contact_us_view_hp(request):
    HTML_STRING = render_to_string("pages/contact_hp.html")
    return HttpResponse (HTML_STRING)

def contact_us_view_ws(request):
    HTML_STRING = render_to_string("pages/contact_ws.html")
    return HttpResponse (HTML_STRING)

#Alt About Pages
def about_view_gso(request):
    HTML_STRING = render_to_string("pages/about_gso.html")
    return HttpResponse (HTML_STRING)

def about_view_hp(request):
    HTML_STRING = render_to_string("pages/about_hp.html")
    return HttpResponse (HTML_STRING)

def about_view_ws(request):
    HTML_STRING = render_to_string("pages/about_ws.html")
    return HttpResponse (HTML_STRING)

def request_offer_view(request):
    HTML_STRING = render_to_string("pages/request_offer.html")
    return HttpResponse (HTML_STRING)
    