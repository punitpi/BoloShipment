from django.db import models

class Shipments(models.Model):
    shipmentId = models.IntegerField(max_length=30)
    shipmentDate = models.DateTimeField(max_length=35)
    shipmentReference = models.CharField(max_length=30)


class shipmentItems(models.Model):
    orderItemId = models.IntegerField(max_length=30)
    orderId = models.IntegerField(max_length=30)
    orderDate = models.DateTimeField(max_length=35)
    latestDeliveryDate = models.DateTimeField(max_length=35)
    ean = models.IntegerField(max_length=20)
    title = models.CharField(max_length=250)
    quantity = models.IntegerField(max_length=10)
    offerPrice = models.FloatField(max_length=20)
    offerCondition = models.CharField(max_length=10)
    offerReference = models.CharField(max_length=30)
    fulfilmentMethod = models.CharField(max_length=10)


class Transport(models.Model):
    transportId =  models.IntegerField(max_length=30)
    transporterCode = models.CharField(max_length=10)
    trackAndTrace = models.CharField(max_length=30)
    shippingLabelId = models.IntegerField(max_length=30)
    shippingLabelCode = models.CharField(max_length=30)


class CustomerDetails(models.Model):
    salutationCode = models.IntegerField(max_length=10)
    firstName = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    streetName = models.CharField(max_length=50)
    houseNumber = models.IntegerField(max_length=10)
    houseNumberExtended = models.CharField(max_length=5)
    addressSupplement = models.CharField(max_length=50)
    extraAddressInformation = models.CharField(max_length=50)
    zipCode = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    countryCode = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    vatNumber = models.CharField(max_length=50)
    chamberOfCommerceNumber = models.IntegerField(max_length=30)
    orderReference = models.CharField(max_length=50)
    deliveryPhoneNumber = models.IntegerField(max_length=17)


class BillingDetails(models.Model):
    salutationCode = models.IntegerField(max_length=10)
    firstName = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    streetName = models.CharField(max_length=50)
    houseNumber = models.IntegerField(max_length=10)
    houseNumberExtended = models.CharField(max_length=5)
    addressSupplement = models.CharField(max_length=50)
    extraAddressInformation = models.CharField(max_length=50)
    zipCode = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    countryCode = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    vatNumber = models.CharField(max_length=50)
    chamberOfCommerceNumber = models.IntegerField(max_length=30)
    orderReference = models.CharField(max_length=50)
    deliveryPhoneNumber = models.IntegerField(max_length=17)


