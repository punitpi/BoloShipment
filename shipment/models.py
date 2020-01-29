from django.db import models
import time
import requests

# Create your models here.
class tokenRefresher():
    host = "https://login.bol.com/token?grant_type=client_credentials"
    client_id = "86b40eb4-ecf5-4c5d-9c20-bd47e85684b8"
    client_secret = "AU9zaVLOLhua7C3UpJcdmCkWvVZSDn9fh9JGxpXoP6mZYxMRwlBhLQ1sb0VILk7DWsTxM4jKXKZaxWogb0J_NA"
    access_token = None
    access_token_expiration = None
    
    def __init__(self, host, key, secret):
        self.host = host
        self.client_id = key
        self.client_secret = secret
        
        try:
            self.access_token, self.access_token_expiration = self.getAccessToken()
        except Exception as e:
            print(e)
    
    def getAccessToken(self):
        payload = 'client_id=' + self.client_id + '&' + 'client_secret=' + self.client_secret
        headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        try:
            request = requests.posts(self.host, data = payload, headers = headers)
            # optional: raise exception for status code
            request.raise_for_status()
        except Exception as e:
            print(e)
            return None
        else:
            # assuming the response's structure is
            # {"access_token": ""}
            access_token = request.json()['access_token']
            access_token_expiration = request.json()['expires_in']
            return access_token, access_token_expiration 