from django.shortcuts import render
from django.http import HttpResponse
import shipment.tokenRefresh as tr
import shipment.getShipment as gs
import shipment.getShipmentDetails as gsd


# Create your views here.
def index(request):
    tr.getAccessToken()
    gs.getShipments()
    gsd.fetchShipmentDetails()
    return HttpResponse("Got Token")
    #return render(request, 'shipment/index.html')
