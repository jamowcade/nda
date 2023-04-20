from django.urls import path
from app import views


urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot/', views.forgot, name='forgot'),
    path('staffs/', views.staffs, name='staffs'),


    #region Environment

    path('company/', views.company, name='company'), 
    path('network/', views.network, name='network'),
    path('host/', views.host, name='host'),

    #endregion





    path('ports/', views.ports, name='ports'),
    
    path('scan_case/', views.scan_case, name='scan_case'),
    path('compare/', views.compare, name='compare'),
    path('Reports2/', views.Reports2, name='Reports2'),
]