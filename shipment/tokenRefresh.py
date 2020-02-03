import requests 
from datetime import datetime, timedelta
from redis import Redis
from rq import Queue
import django_rq
#from rq_scheduler import Scheduler
r = Redis(host='127.0.0.1', port = 6379, db = 0)

host = r.get('AUTH_HOST').decode('utf-8')
client_id = r.get('CLIENT_ID').decode('utf-8')
client_secret = r.get('CLIENT_SECRET_KEY').decode('utf-8')
accessToken = None
accessTokenExpiration = None



def getAccessToken():    
    payload = 'client_id=' + client_id + '&' + 'client_secret=' + client_secret
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    try:
        #Geting data from the API
        response = requests.request("POST", host, headers = headers, data = payload)
       
        # optional: raise exception for status code
    except Exception as e:
        print(e)
        return None
    else:
        #Adding the token to Redis Cache
        accessToken = response.json()['access_token']
        r.set('access_token', accessToken, 500)
        accessTokenExpiration = response.json()['expires_in']
        scheduleRefreshToken(accessTokenExpiration)
        

def scheduleRefreshToken(accessTokenExpiration):
    #Adding to the schedule
    scheduler = django_rq.get_scheduler('high')
    scheduler.enqueue_in(timedelta(seconds=accessTokenExpiration) , getAccessToken)

    
