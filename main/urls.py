from django.urls import path
from main import views
from .code import Company,User,Network,Hosts,Ports,Scan,Reports,Compare


urlpatterns = [
    path('', views.index, name='index'),

    path('login/', User.login, name='login'),
    path('register/', User.register, name='register'),
    path('forgot/', User.forgot, name='forgot'),
    path('staffs/', User.staffs, name='staffs'),


    #region Environment

    path('company/', Company.company, name='company'), 
    path('network/', Network.network, name='network'),
    path('host/', Hosts.host, name='host'),

    #endregion





    path('ports/', Ports.ports, name='ports'),
    
    path('scan_case/', Scan.scan_case, name='scan_case'),
    path('compare/', Compare.compare, name='compare'),
    path('reports/', Reports.Reports, name='reports'),
]