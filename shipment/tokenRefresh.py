import requests 
from datetime import datetime, timedelta
from redis import Redis, StrictRedis
from rq import Queue
from rq_scheduler import Scheduler

host = "https://login.bol.com/token?grant_type=client_credentials"
client_id = "86b40eb4-ecf5-4c5d-9c20-bd47e85684b8"
client_secret = "AU9zaVLOLhua7C3UpJcdmCkWvVZSDn9fh9JGxpXoP6mZYxMRwlBhLQ1sb0VILk7DWsTxM4jKXKZaxWogb0J_NA"
accessToken = None
accessTokenExpiration = None
tokenExpiryTime = None



def getAccessToken():
    #r = StrictRedis(host='localhost', port=6379, db=1)
    r = Redis(host='127.0.0.1', port = 6379, db = 0)
    
    payload = 'client_id=' + client_id + '&' + 'client_secret=' + client_secret
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    try:
        response = requests.request("POST", host, headers = headers, data = payload)
       
        # optional: raise exception for status code
    except Exception as e:
        print(e)
        return None
    else:
        
        now = datetime.utcnow()
        accessToken = response.json()['access_token']
        r.set('access_token', accessToken, 500)
        accessTokenExpiration = response.json()['expires_in']
        now += timedelta(seconds=accessTokenExpiration) 
        
        tokenExpiryTime = now
        refreshToken(accessTokenExpiration)
        

def refreshToken(accessTokenExpiration):
    scheduler = Scheduler(connection=Redis())
    scheduler.enqueue_in(timedelta(seconds=accessTokenExpiration) , getAccessToken)

    