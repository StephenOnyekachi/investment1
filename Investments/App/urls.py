from django.urls import path

from . import views

urlpatterns = [
    path('login', views.UserLogin, name="login"),
    path('logout', views.UserLogout, name="logout"),
    path('', views.Index, name='home'),
    path('signup', views.SignUp, name='signup'),

    path('adminview',views.AdminView, name="adminview"),
    path('dashboard',views.DashboardView, name="dashboard"),

    path('withdraw', views.Withdraw, name='withdraw'),
    path('upgrade', views.Upgrade, name='upgrade'),
    path('mes', views.Mes, name='mes'),
    path('sms', views.Sms, name='sms'),
    path('payment/<int:pk>/', views.Payment, name='payment'),
    path('bankinfo', views.Bankinfo, name='bankinfo'),
    path('userinfo', views.Userinfo, name='userinfo'),
    path('history', views.History, name='history'),

    path('edituser/<int:pk>/', views.EditUser, name='edituser'),
    path('deleteuser/<int:pk>/', views.DeleteUser, name='deleteuser'),
    path('block/<int:pk>/', views.Block, name='block'),
    path('approve/<int:pk>/', views.Approve, name='approve'),

    path('planedit/<int:pk>/', views.PlanEdit, name='planedit'),
    path('plandelete/<int:pk>/', views.PlanDelete, name='plandelete'),
    # path('pdf', views.pdf, name="pdf"),


    # path('edittable/<int:pk>/', views.EditTable, name='edittable'),
    # path('deletetable/<int:pk>/', views.DeleteTable, name='deletetable'),


    # path('chart', views.Charts, name='chart'),
    
]

