from django.urls import path
from main import views
from .code import company,user,Network,Hosts,Ports,Reports,Compare, scan_case, groups, logs


urlpatterns = [
    path('', views.index, name='index'),

    path('login/', user.login_user, name='login'),
    path('register/', user.register, name='register'),
    path('forgot/', user.forgot, name='forgot'),
    path('logout/', user.logout_user, name='logout'),
    path('users/', user.users, name='users'),
    path("myprofile/",user.myprofile, name="myprofile"),
    path("changepassword/",user.changepassword, name="changepassword"),
    path('activeAccount/', user.activeAccount, name='activeAccount'),
    path('disableAccount/', user.disableAccount, name='disableAccount'),
    path('editAccount/', user.updateAccount, name='editAccount'),

    #region Environment

    path('company/', company.company, name='company'), 
    path('networks/', Network.networkDetails, name='networks'),
    path('all_networks/', Network.all_networks, name='all_networks'),
    path('network/<int:id>/', Network.networkDetails, name='network'),
    # path('host/', Hosts.host, name='host'),
    path('host/<int:id>/', Hosts.host, name='host'),
    path('getport_service/', Hosts.search, name='getport_service'),
    path('uploadhosts/', Hosts.addHosts, name='uploadhosts'),
    path('addnetwork/', Network.addNetwork, name='add_network'),
    path('updateNetwork/', Network.updateNetwork, name='update_network'),
    path('scan_case/<int:scan_case_id>/', scan_case.delete_scan_case, name='delete_scan_case'),

    #endregion





    path('host_ports/', Ports.ports, name='ports'),
    # path('host_ports/<int:id>/', Ports.ports, name='ports'),
    
    path('scan_case/', scan_case.scan_case, name='scan_case'),
    path('compare/', Compare.compare, name='compare'),

    path('filter_data/', Reports.filter_data, name='filter_data'),


    path('filter_by_date/', Compare.filter_by_date, name='filter_by_date'),
    path('compare_by_date/', Compare.compare_by_date, name='compare_by_date'),
    path('showdetail/', Compare.showdetaile, name='showdetail'),
    path('get_Hosts/', Compare.get_Hosts, name='get_Hosts'),






    # path('compare2_by_date/', Compare.compare2_by_date, name='compare2_by_date'),
    path('get_campany_name/', Compare.get_campany_name, name='get_campany_name'),

    path('scan_cases_report/', Reports.scan_cases_report, name='scan_cases_report'),
    path('scan_case_report/', Reports.scan_case_report, name='scan_case_report'),
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

    # error logs
    path("erorlogs/",logs.erorlogs, name="erorlogs"),
    path("userlogs/",logs.userlogs, name="userlogs"),

    # compare and reports.





    ]