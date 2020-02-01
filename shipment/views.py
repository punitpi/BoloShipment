from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
import shipment.tokenRefresh as tr
import shipment.getShipment as gs
import shipment.getShipmentDetails as gsd
import shipment.getAPIHosts as api
from .models import Shipments, ShipmentItems, BillingDetails, CustomerDetails, Transport


# Create your views here.
def index(request):
    api.get_secret_setting()
    tr.getAccessToken()
    gs.scheduleShip(1)
    gsd.scheduleShipdetails(10)  
    return render(request, 'shipment/index.html')

def shipdetail(request):
    gs.getShipments()
    gsd.scheduleShipdetails(1)
    query_results = Shipments.objects.all()
    return render(request, 'shipment/shipdetail.html', {'query_results': query_results})

def customer(request):
    gsd.fetchShipmentDetails()
    query_results1 = BillingDetails.objects.all()
    query_results2 = CustomerDetails.objects.all()
    return render(request, 'shipment/customer.html', {'query_results1': query_results1, 'query_results2': query_results2})
    

def transport(request):
    query_results = Transport.objects.all()
    return render(request, 'shipment/transport.html', {'query_results': query_results})