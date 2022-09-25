from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    #login, logout and signup
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('signup/', views.signup_user, name="signup"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('toDoAdd/', views.toDoAdd, name="add"),
    path('toDoUpdate/<str:id>', views.toDoUpdate, name="update"),
    path('toDoDelete/<str:id>', views.toDoDelete, name="delete"),
]
