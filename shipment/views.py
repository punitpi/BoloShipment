from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
import shipment.tokenRefresh as tr
import shipment.getShipment as gs
import shipment.getShipmentDetails as gsd
from redis import Redis
from .models import Shipments, ShipmentItems, BillingDetails, CustomerDetails, Transport

r = Redis(host='127.0.0.1', port = 6379, db = 0)

def index(request):
    tr.getAccessToken()
    gs.scheduleShip(1)
    gsd.scheduleShipdetails(1)  
    return render(request, 'shipment/index.html')

#Get shipment details from the shipment/* API
def shipdetail(request):
    if r.get('getShipment') == None:
        gsd.scheduleShipdetails(60)
        gs.getShipments()
    query_results = Shipments.objects.all()
    return render(request, 'shipment/shipdetail.html', {'query_results': query_results})

#Get Customer Details from the shipment/* API
def customer(request):
    if r.get('getShipmentDetails') == None:
        gsd.fetchShipmentDetails()
    query_results1 = BillingDetails.objects.all()
    query_results2 = CustomerDetails.objects.all()
    return render(request, 'shipment/customer.html', {'query_results1': query_results1, 'query_results2': query_results2})
    
#Get Transport Details from the shipment/* API
def transport(request):
    if r.get('getShipmentDetails') == None:
        gsd.fetchShipmentDetails()
    query_results = Transport.objects.all()
    return render(request, 'shipment/transport.html', {'query_results': query_results})
