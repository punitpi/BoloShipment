import requests 
import json
from datetime import datetime, timedelta
from redis import Redis
from rq import Queue
#from rq_scheduler import Scheduler
import django_rq
from shipment.models import Shipments, ShipmentItems, BillingDetails, CustomerDetails, Transport
from django.db.models import *
from django.db.models.functions import *

r = Redis(host='127.0.0.1', port = 6379, db = 0)
host = r.get('SHIPMENT_HOST').decode('utf-8')

def fetchShipmentDetails():
    
    #r = StrictRedis(host='localhost', port=6379, db=1)
    #r = Redis(host='127.0.0.1', port = 6379, db = 0)
    headers = {
    'Accept': 'application/vnd.retailer.v3+json',
    'Authorization': 'Bearer ' + r.get('access_token').decode('utf-8')
    }
    try:
        response = None
        ids = r.get('shipmentId')
        if ids != None:
            ids = ids.decode('utf-8').split(",")
        jsonKeys = ['shipmentItems','transport','customerDetails','billingDetails']
        
        for id in ids:
            url = host + '' + defaultponse.json()
            now = datetime.now()
            for key in jsonKeys:
                jsonItems = jsonResponse[key]
                shipmentId = ''
                obj = ''
                if key == 'shipmentItems':
                    for jsonItem in jsonItems:
                        flag = ShipmentItems.objects.filter(shipmentId = jsonResponse['shipmentId'], orderItemId = jsonItem['orderItemId'], orderId = jsonItem['orderId'], orderDate = jsonItem['orderDate'], latestDeliveryDate = jsonItem['latestDeliveryDate'], ean = jsonItem['ean'], title = jsonItem['title'], quantity = jsonItem['quantity'], offerPrice = jsonItem['offerPrice'], offerCondition = jsonItem['offerCondition'], fulfilmentMethod = jsonItem['fulfilmentMethod']).exists()
                        if not flag:
                            obj = ShipmentItems.objects.create(shipmentId = jsonResponse['shipmentId'], orderItemId = jsonItem['orderItemId'], orderId = jsonItem['orderId'], orderDate = jsonItem['orderDate'], latestDeliveryDate = jsonItem['latestDeliveryDate'], ean = jsonItem['ean'], title = jsonItem['title'], quantity = jsonItem['quantity'], offerPrice = jsonItem['offerPrice'], offerCondition = jsonItem['offerCondition'], fulfilmentMethod = jsonItem['fulfilmentMethod'])
                        
                if key == 'transport':
                    val = str(jsonItems)
                    shippingLabelCodetext = '' if val.find('shippingLabelCode') == -1 else jsonItems['shippingLabelCode']
                    shippingLabelIdtext = -1 if val.find('shippingLabelId') == -1 else jsonItems['shippingLabelId']
                    trackAndTracetext = -1 if val.find('trackAndTrace') == -1 else jsonItems['trackAndTrace']
                    flag = Transport.objects.filter(shipmentId = jsonResponse['shipmentId'], transportId = jsonItems['transportId'], transporterCode = jsonItems['transporterCode'], trackAndTrace = trackAndTracetext, shippingLabelId = shippingLabelIdtext, shippingLabelCode = shippingLabelCodetext).exists()
                    if not flag:
                        obj = Transport.objects.create(shipmentId = jsonResponse['shipmentId'], transportId = jsonItems['transportId'], transporterCode = jsonItems['transporterCode'], trackAndTrace = trackAndTracetext, shippingLabelId = shippingLabelIdtext, shippingLabelCode = shippingLabelCodetext)
                    
                if key == 'customerDetails':
                    val = str(jsonItems)
                    houseNumberExtendedtext = '' if val.find('houseNumberExtended') == -1 else jsonItems['houseNumberExtended']
                    addressSupplementtext = '' if val.find('addressSupplement') == -1 else jsonItems['addressSupplement']
                    extraAddressInformationtext = '' if val.find('extraAddressInformation') == -1 else jsonItems['extraAddressInformation']
                    companytext = ''  if val.find('company') == -1 else jsonItems['company']
                    vatNumbertext = ''  if val.find('vatNumber') == -1 else jsonItems['vatNumber']
                    chamberOfCommerceNumbertext = -1 if val.find('chamberOfCommerceNumber') == -1 else jsonItems['chamberOfCommerceNumber']
                    orderReferencetext = ''  if val.find('orderReference') == -1 else jsonItems['orderReference']
                    deliveryPhoneNumbertext = -1 if val.find('deliveryPhoneNumber') == -1 else jsonItems['deliveryPhoneNumber']
                    flag = CustomerDetails.objects.filter(shipmentId = jsonResponse['shipmentId'], salutationCode = jsonItems['salutationCode'], firstName = jsonItems['firstName'], surname = jsonItems['surname'], streetName = jsonItems['streetName'], houseNumber = jsonItems['houseNumber'], houseNumberExtended = houseNumberExtendedtext, addressSupplement = addressSupplementtext, extraAddressInformation = extraAddressInformationtext, zipCode = jsonItems['zipCode'], city = jsonItems['city'], countryCode = jsonItems['countryCode'], email = jsonItems['email'], company = companytext, vatNumber = vatNumbertext, chamberOfCommerceNumber = chamberOfCommerceNumbertext, orderReference = orderReferencetext, deliveryPhoneNumber = deliveryPhoneNumbertext).exists()
                    if not flag:
                        obj = CustomerDetails.objects.create(shipmentId = jsonResponse['shipmentId'], salutationCode = jsonItems['salutationCode'], firstName = jsonItems['firstName'], surname = jsonItems['surname'], streetName = jsonItems['streetName'], houseNumber = jsonItems['houseNumber'], houseNumberExtended = houseNumberExtendedtext, addressSupplement = addressSupplementtext, extraAddressInformation = extraAddressInformationtext, zipCode = jsonItems['zipCode'], city = jsonItems['city'], countryCode = jsonItems['countryCode'], email = jsonItems['email'], company = companytext, vatNumber = vatNumbertext, chamberOfCommerceNumber = chamberOfCommerceNumbertext, orderReference = orderReferencetext, deliveryPhoneNumber = deliveryPhoneNumbertext)
                
                if key =='billingDetails':
                    val = str(jsonItems)
                    houseNumberExtendedtext = '' if val.find('houseNumberExtended') == -1 else jsonItems['houseNumberExtended']
                    addressSupplementtext = '' if val.find('addressSupplement') == -1 else jsonItems['addressSupplement']
                    extraAddressInformationtext = '' if val.find('extraAddressInformation') == -1 else jsonItems['extraAddressInformation']
                    companytext = ''  if val.find('company') == -1 else jsonItems['company']
                    vatNumbertext = ''  if val.find('vatNumber') == -1 else jsonItems['vatNumber']
                    chamberOfCommerceNumbertext = -1 if val.find('chamberOfCommerceNumber') == -1 else jsonItems['chamberOfCommerceNumber']
                    orderReferencetext = ''  if val.find('orderReference') == -1 else jsonItems['orderReference']
                    deliveryPhoneNumbertext = -1 if val.find('deliveryPhoneNumber') == -1 else jsonItems['deliveryPhoneNumber']
                    flag = BillingDetails.objects.filter(shipmentId = jsonResponse['shipmentId'], salutationCode = jsonItems['salutationCode'], firstName = jsonItems['firstName'], surname = jsonItems['surname'], streetName = jsonItems['streetName'], houseNumber = jsonItems['houseNumber'], houseNumberExtended = houseNumberExtendedtext, addressSupplement = addressSupplementtext, extraAddressInformation = extraAddressInformationtext, zipCode = jsonItems['zipCode'], city = jsonItems['city'], countryCode = jsonItems['countryCode'], email = jsonItems['email'], company = companytext, vatNumber = vatNumbertext, chamberOfCommerceNumber = chamberOfCommerceNumbertext, orderReference = orderReferencetext, deliveryPhoneNumber = deliveryPhoneNumbertext).exists()
                    if not flag:
                        obj = BillingDetails.objects.create(shipmentId = jsonResponse['shipmentId'], salutationCode = jsonItems['salutationCode'], firstName = jsonItems['firstName'], surname = jsonItems['surname'], streetName = jsonItems['streetName'], houseNumber = jsonItems['houseNumber'], houseNumberExtended = houseNumberExtendedtext, addressSupplement = addressSupplementtext, extraAddressInformation = extraAddressInformationtext, zipCode = jsonItems['zipCode'], city = jsonItems['city'], countryCode = jsonItems['countryCode'], email = jsonItems['email'], company = companytext, vatNumber = vatNumbertext, chamberOfCommerceNumber = chamberOfCommerceNumbertext, orderReference = orderReferencetext, deliveryPhoneNumber = deliveryPhoneNumbertext)
                if obj != '':
                    obj.save()
                
                    
                
        #scheduleShipdetails(now + timedelta(minutes = 1))
        scheduleShipdetails(120)
            
        
        # optional: raise exception for status code
    except Exception as e:
        print(e)
        return None
        
        

def scheduleShipdetails(schTime):
    #scheduler = Scheduler(connection=Redis())
    scheduler = django_rq.get_scheduler('default')
    scheduler.enqueue_in(timedelta(seconds=schTime) , fetchShipmentDetails)
