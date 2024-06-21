from django.urls import path,include
from rest_framework import routers
from api import views
'''
router = routers.DefaultRouter()
router.register(r'usuarios',views.UsuarioViewSet)'''

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('prueba/',views.PruebaView, name="prueba"),
    path('add/', views.UsuarioAdd, name="user_add"),
    path('listar/', views.ListarUsuarios, name="listar"),
    path('validar/', views.ValidarUsuario, name="validar"),
    path('login/', views.LoginUsuario, name="login"),
    path('register/', views.RegisterUsuario, name="register"),
    
]