from django.shortcuts import render
import shipment.tokenRefresh as tr
from django.http import HttpResponse


# Create your views here.
def index(request):
    tr.getAccessToken()
    
    return HttpResponse("Got Token")
    #return render(request, 'shipment/index.html')