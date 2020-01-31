from datetime import datetime, timedelta
from redis import Redis
from rq import Queue
from rq_scheduler import Scheduler
import shipment.tokenRefresh 

scheduler = Scheduler(connection=Redis()) # Get a scheduler for the "default" queue

#def addIn():
    #tim = datetime.utcnow()
    #tim = tim + timedelta(seconds=10)
    #scheduler.enqueue_at(tim , shipment.tokenRefresh.getAccessToken)