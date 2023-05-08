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
    path('networks/', Network.networkDetails, name='networks'),
    path('all_networks/', Network.all_networks, name='all_networks'),
    path('network/<int:id>/', Network.networkDetails, name='network'),
    # path('host/', Hosts.host, name='host'),
    path('host/<int:id>/', Hosts.host, name='host'),
    path('uploadhosts/', Hosts.addHosts, name='uploadhosts'),
    path('addnetwork/', Network.addNetwork, name='add_network'),
    path('updateNetwork/', Network.updateNetwork, name='update_network'),

    #endregion





    path('host_ports/', Ports.ports, name='ports'),
    # path('host_ports/<int:id>/', Ports.ports, name='ports'),
    
    path('scan_case/', Scan.scan_case, name='scan_case'),
    path('compare/', Compare.compare, name='compare'),
    path('filter_by_date/', Compare.filter_by_date, name='filter_by_date'),
    path('reports/', Reports.Reports, name='reports'),
    path('newCompany/', company.createCompany, name='add_company'),
    path('editCompany/', company.editCompany, name='edit_company'),
]