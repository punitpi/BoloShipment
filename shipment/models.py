from django.db import models


class CustomerDetails(models.Model):
    shipmentId = models.IntegerField(max_length=30)
    salutationCode = models.CharField(max_length=10)
    firstName = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    streetName = models.CharField(max_length=50)
    houseNumber = models.CharField(max_length=10)
    houseNumberExtended = models.CharField(max_length=5, null=True)
    addressSupplement = models.CharField(max_length=50, null=True)
    extraAddressInformation = models.CharField(max_length=50, null=True)
    zipCode = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    countryCode = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    company = models.CharField(max_length=50, null=True)
    vatNumber = models.CharField(max_length=50, null=True)
    chamberOfCommerceNumber = models.CharField(max_length=30, null=True)
    orderReference = models.CharField(max_length=50, null=True)
    deliveryPhoneNumber = models.CharField(max_length=17, null=True)
    def __str__(self):
        return self.shipmentId

class BillingDetails(models.Model):
    shipmentId = models.IntegerField(max_length=30)
    salutationCode = models.CharField(max_length=10)
    firstName = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    streetName = models.CharField(max_length=50)
    houseNumber = models.CharField(max_length=10)
    houseNumberExtended = models.CharField(max_length=5, null=True)
    addressSupplement = models.CharField(max_length=50, null=True)
    extraAddressInformation = models.CharField(max_length=50, null=True)
    zipCode = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    countryCode = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    company = models.CharField(max_length=50, null=True)
    vatNumber = models.CharField(max_length=50, null=True)
    chamberOfCommerceNumber = models.CharField(max_length=30, null=True)
    orderReference = models.CharField(max_length=50, null=True)
    deliveryPhoneNumber = models.CharField(max_length=17, null=True)
    def __str__(self):
        return self.shipmentId

class Shipments(models.Model):
    shipmentId = models.IntegerField(max_length=30, unique=True)
    shipmentDate = models.DateTimeField(max_length=35)
    shipmentDate = models.CharField(max_length=30, null=True)

class ShipmentItems(models.Model):
    shipmentId = models.IntegerField(max_length=30)
    orderItemId = models.CharField(max_length=30)
    orderId = models.CharField(max_length=30)
    orderDate = models.DateTimeField(max_length=35)
    latestDeliveryDate = models.DateTimeField(max_length=35)
    ean = models.CharField(max_length=20)
    title = models.CharField(max_length=250)
    quantity = models.IntegerField(max_length=10)
    offerPrice = models.FloatField(max_length=20)
    offerCondition = models.CharField(max_length=10)
    offerReference = models.CharField(max_length=30, null=True)
    fulfilmentMethod = models.CharField(max_length=10)
    def __str__(self):
        return self.shipmentId

class Transport(models.Model):
    shipmentId = models.IntegerField(max_length=30)
    transportId =  models.IntegerField(max_length=30)
    transporterCode = models.CharField(max_length=10)
    trackAndTrace = models.CharField(max_length=30)
    shippingLabelId = models.IntegerField(max_length=30, null=True)
    shippingLabelCode = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.shipmentId
