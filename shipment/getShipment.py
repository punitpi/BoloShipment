import requests 
from datetime import datetime, timedelta
from redis import Redis, StrictRedis
from rq import Queue
from rq_scheduler import Scheduler

