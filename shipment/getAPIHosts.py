import os, json
from redis import Redis

with open(os.path.abspath("django-secrets.json")) as f:
    secrets = json.loads(f.read())
 
 
def get_secret_setting():

    r = Redis(host='127.0.0.1', port = 6379, db = 0)

    r.set('SHIPMENT_HOST', secrets['SHIPMENT_HOST'], ex=None)
    r.set('AUTH_HOST', secrets['AUTH_HOST'], ex=None)
    r.set('CLIENT_ID', secrets['CLIENT_ID'], ex=None) 
    r.set('CLIENT_SECRET_KEY', secrets['CLIENT_SECRET_KEY'], ex=None)
    
