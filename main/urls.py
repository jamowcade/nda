from django.urls import path
from main import views
from .code import user,company


urlpatterns = [
    path('', views.index, name='index'),

    path('login/', user.login, name='login'),
    path('register/', user.register, name='register'),
    path('forgot/', user.forgot, name='forgot'),
    path('staffs/', user.staffs, name='staffs'),


    #region Environment

    path('company/', company.company, name='company'), 
    path('network/', views.network, name='network'),
    path('host/', views.host, name='host'),

    #endregion





    path('ports/', views.ports, name='ports'),
    
    path('scan_case/', views.scan_case, name='scan_case'),
    path('compare/', views.compare, name='compare'),
    path('Reports2/', views.Reports2, name='Reports2'),
]