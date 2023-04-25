from django.urls import path
from main import views
from .code import company,user,Network,Hosts,Ports,Scan,Reports,Compare


urlpatterns = [
    path('', views.index, name='index'),

    path('login/', user.login, name='login'),
    path('register/', user.register, name='register'),
    path('forgot/', user.forgot, name='forgot'),
    path('staffs/', user.staffs, name='staffs'),


    #region Environment

    path('company/', company.company, name='company'), 
    path('networks/', Network.network, name='networks'),
    path('network/<int:id>/', Network.network, name='network'),
    path('host/', Hosts.host, name='host'),

    #endregion





    path('ports/', Ports.ports, name='ports'),
    
    path('scan_case/', Scan.scan_case, name='scan_case'),
    path('compare/', Compare.compare, name='compare'),
    path('reports/', Reports.Reports, name='reports'),
]