from django.db import models
from datetime import datetime
# Create your models here.
from django.contrib.auth.models import AbstractUser


class Campany(models.Model):
    title = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    timestamp = models.DateField(auto_now_add=True)
    asn = models.CharField(max_length=100)


    def __str__(self):
        return self.owner



class Network(models.Model):
    OPEN = 'O'
    CLOSE = 'C'
    PAYMENT_STATUS_CHOICES = [
        (OPEN, 'OPEN'),
        (CLOSE, 'CLOSE')
    ]

    state = models.CharField(max_length=50,choices=PAYMENT_STATUS_CHOICES, default=OPEN)
    network = models.CharField(max_length=50)
    time = models.DateField(auto_now_add=True)
    compony_info = models.ForeignKey(Campany, on_delete=models.CASCADE,related_name='networks')
    description = models.CharField(max_length=500)
    

    
    def __str__(self):
        return self.network




class Host(models.Model):
    hostname = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    host_date = models.DateField(auto_now=False, auto_now_add=False, default=False)
    network = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='hosts')
    reason = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.hostname
    



class Port(models.Model):
    port = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    protocol = models.CharField(max_length=50,null=True)
    reason = models.CharField(max_length=50, null=True)
    service = models.CharField(max_length=50,null=True)
    rpc_info = models.CharField(max_length=50,null=True)
    version = models.CharField(max_length=50,null=True)
    host = models.ForeignKey(Host, on_delete=models.CASCADE,related_name='ports')
                    

class ScanCase(models.Model):
    scan_date = models.DateField(auto_now=False, auto_now_add=False, default=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)