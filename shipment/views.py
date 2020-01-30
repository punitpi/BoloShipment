from django.shortcuts import render
from django.http import HttpResponse
import shipment.tokenRefresh as tr
import shipment.getShipment as gs


# Create your views here.
def index(request):
    tr.getAccessToken()
    gs.getShipments()
    return HttpResponse("Got Token")
    #return render(request, 'shipment/index.html')
