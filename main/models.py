from django.db import models
from datetime import datetime
# Create your models here.
from django.contrib.auth.models import AbstractUser, User



class ScanCase(models.Model):
    scan_date = models.DateField(auto_now=False, auto_now_add=False, default=False,unique=True)
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    class Meta:
        permissions = [
            ("can_compare_scancase", "Can compare Scancase"),
        ]

    

class Campany(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    timestamp = models.DateField(auto_now_add=True)
    asn = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.owner

    def totalNetworks(self):
        total_networks = self.networks.all().count()
        return total_networks

class Network(models.Model):
    OPEN = 'O'
    CLOSE = 'C'
    PAYMENT_STATUS_CHOICES = [
        (OPEN, 'OPEN'),
        (CLOSE, 'CLOSE')
    ]

    state = models.CharField(max_length=50,choices=PAYMENT_STATUS_CHOICES, default=OPEN)
    network = models.CharField(max_length=50,unique=True)
    time = models.DateField(auto_now_add=True)
    compony_info = models.ForeignKey(Campany, on_delete=models.CASCADE,related_name='networks')
    description = models.CharField(max_length=500)
    

    
    def __str__(self):
        return self.network
    
    def totalHosts(self):
        total_hosts = self.hosts.all().count()
        return total_hosts
 



class Host(models.Model):
    hostname = models.CharField(max_length=500)
    status = models.CharField(max_length=500)
    host_date = models.DateField(auto_now=False, auto_now_add=False, default=False)
    network = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='hosts')
    scan_case = models.ForeignKey(ScanCase, on_delete=models.CASCADE, related_name='hosts', null=True)
    reason = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.hostname
    
    def closedPorts(self):
        closed_ports = self.ports.filter(state="closed").all().count()
        return closed_ports

    def openPorts(self):
        open_ports = self.ports.filter(state="open").all().count()
        return open_ports

    def filteredPorts(self):
        filtered_ports = self.ports.filter(state="filtered").all().count()
        return filtered_ports

    

    def totalPorts(self):
        totalPorts = self.ports.all().count()
        return totalPorts
    
    def getPorts(self, state):
        ports = self.ports.filter(state=state).all()
        return ports



class Port(models.Model):
    port = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    protocol = models.CharField(max_length=50,null=True)
    reason = models.CharField(max_length=50, null=True)
    host = models.ForeignKey(Host, on_delete=models.CASCADE,related_name='ports')

class Service(models.Model):
    key = models.CharField(max_length=150,null=True)
    value = models.CharField(max_length=500,null=True)
    port = models.ForeignKey(Port, on_delete=models.CASCADE,related_name='services')
                    


class ErrorLog(models.Model):
    user = models.CharField(max_length=30)
    device = models.TextField(null=True)
    message = models.CharField(max_length=255)
    info = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

class UserLog(models.Model):
    user = models.TextField()
    device = models.TextField(null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    

