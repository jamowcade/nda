from django.urls import path
from main import views
from .code import company,user,Network,Hosts,Ports,Reports,Compare, scan_case, groups


urlpatterns = [
    path('', views.index, name='index'),

    path('login/', user.login_user, name='login'),
    path('register/', user.register, name='register'),
    path('forgot/', user.forgot, name='forgot'),
    path('logout/', user.logout_user, name='logout'),
    path('users/', user.users, name='users'),

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
    
    path('scan_case/', scan_case.scan_case, name='scan_case'),
    path('compare/', Compare.compare, name='compare'),
    path('filter_by_date/', Compare.filter_by_date, name='filter_by_date'),
    path('reports/', Reports.Reports, name='reports'),
    path('scan_cases_report/', Reports.scan_cases_report, name='scan_cases_report'),
    path('newCompany/', company.createCompany, name='add_company'),
    path('editCompany/', company.editCompany, name='edit_company'),



    # groups and permissions.
    path("permissions/",user.permissions, name="permissions"),
    path('groups/', groups.groups, name='groups'),
    path('user_groups/', groups.user_groups, name='user_groups'),
    path('assign_user_to_groups/', groups.assign_user_to_groups, name='assign_user_to_groups'),
    path('get_user_groups/', groups.get_user_groups, name='get_user_groups'),

    # group permissions
    path("assign_permissions_to_group/",groups.assign_permissions_to_group, name="assign_permissions_to_group"),
    path("get_permissions/",groups.get_permissions, name="get_permissions"),
    path("groupPermissions/",groups.groupPermissions, name="group_Permissions"),
    path("get_group_permissions/",groups.get_group_permissions, name="get_group_permissions"),

    #user permissions
    path("get-user-info/",user.get_user_info, name="get-user-info"),
    path("get_permissions_user/",user.get_permissions_user, name="get_permissions_user"),
    path("get_user_permissions/",user.get_user_permissions, name="get_user_permissions"),
    path("assign_permissions_to_user/",user.assign_permissions_to_user, name="assign_permissions_to_user"),

    # compare and reports.





    ]