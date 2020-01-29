from django.db import models

# Create your models here.
class myAPI():
    host = None
    key = None
    secret = None
    client_id = None
    client_secret = None
    def __init__(self):
        super().__init__()