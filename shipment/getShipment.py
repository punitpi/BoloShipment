import requests 
import json
from datetime import datetime, timedelta
from redis import Redis, StrictRedis
from rq import Queue
from rq_scheduler import Scheduler
from .models import Shipments
from django.db.models import *
from django.db.models.functions import *
from django.http import JsonResponse
 
host = "https://api.bol.com/retailer/shipments"


def getShipments():
    #r = StrictRedis(host='localhost', port=6379, db=1)
    r = Redis(host='127.0.0.1', port = 6379, db = 0)
    headers = {
    'Accept': 'application/vnd.retailer.v3+json',
    'Authorization': 'Bearer ' + r.get('access_token').decode('utf-8')
    }
    try:
        now = datetime.now()
        response = requests.request("GET", host, headers = headers)
       
        # optional: raise exception for status code
    except Exception as e:
        print(e)
        return None
    else:
        jsonResponse = response.json()
        shipmentsjson = jsonResponse['shipments']
        shipmentId = None
        for shipment in shipmentsjson:
            obj = Shipments.objects.create(shipmentId = shipment['shipmentId'], shipmentDate = shipment['shipmentDate'])
            shipmentId += shipment['shipmentId'] + ','
            obj.save()
        shipmentId = shipmentId[:-1]
        r.set('shipmentId', shipmentId, 90)
        scheduleShip(now + timedelta(minutes = 2))
        

def scheduleShip(schTime):
    scheduler = Scheduler(connection=Redis())
    scheduler.enqueue_at(schTime , getAccessToken)
