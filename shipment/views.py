from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
import shipment.tokenRefresh as tr
import shipment.getShipment as gs
import shipment.getShipmentDetails as gsd
from .models import Shipments, ShipmentItems, BillingDetails, CustomerDetails, Transport


# Create your views here.
def index(request):
    tr.getAccessToken()
    gs.getShipments()
    gsd.scheduleShipdetails(datetime.now() + timedelta(seconds=10))
    query_results = Shipments.objects.all()
    return render(request, 'shipment/index.html', {'query_results': query_results})

def customer(request):
    query_results = BillingDetails.objects.all()
    query_results1 = CustomerDetails.objects.all()
    return render(request, 'shipment/customer.html')
    
def shipstatus(request):
    query_results = Shipments.objects.all()
    return render(request, 'shipment/shipstatus.html')

def transport(request):
    query_results = Shipments.objects.all()
    return render(request, 'shipment/transport.html')