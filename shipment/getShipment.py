import requests 
import json
from datetime import datetime, timedelta
from redis import Redis
from rq import Queue
#from rq_scheduler import Scheduler
import django_rq
from shipment.models import Shipments
from django.db.models import *
from django.db.models.functions import *

 
r = Redis(host='127.0.0.1', port = 6379, db = 0)
host = r.get('SHIPMENT_HOST').decode('utf-8')

def getShipments():
    #r = StrictRedis(host='localhost', port=6379, db=1)
    #r = Redis(host='127.0.0.1', port = 6379, db = 0)
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
        shipmentId = ''
        ids = r.get('shipmentId')
        if ids != None: 
            ids = ids.decode('utf-8').split(",")
        for shipment in shipmentsjson:
            shipmentId = shipmentId + str(shipment['shipmentId']) + ','
            if not Shipments.objects.filter(shipmentId = shipment['shipmentId'], shipmentDate = shipment['shipmentDate']).exists():
                obj = Shipments.objects.create(shipmentId = shipment['shipmentId'], shipmentDate = shipment['shipmentDate'])
                shipmentId = shipmentId + str(shipment['shipmentId']) + ','
                obj.save()
            
        
        shipmentId = shipmentId[:-1]
        r.set('shipmentId', shipmentId, 90)
        scheduleShip(60)
        

def scheduleShip(schTime):
    #scheduler = Scheduler(connection=Redis())

    scheduler = django_rq.get_scheduler('high')
    scheduler.enqueue_in(timedelta(seconds=schTime) , getShipments)
