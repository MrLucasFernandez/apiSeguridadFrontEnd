from rest_framework import viewsets
from .serializer import UsuariosSerializer
from .models import Usuario
from api.models import Usuario
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from rest_framework.utils import json
from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
"""
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer"""
    
"""
class Register(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
"""

class IndexView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        return render(request, 'api/index.html')
def PruebaView(request):
    headers = {'x-api-key': 'MuHOjsQ76J1ImP5QU4XyD27QdeieqTH589NbU3Uo','Content-Type': 'text/html; charset=utf-8'}
    response = requests.get('https://qic534o8o0.execute-api.us-east-1.amazonaws.com/ventas/documentacion', headers=headers)
    return HttpResponse(response.content)

def LoginUsuario(request):
    return render(request, 'api/login.html')
def RegisterUsuario(request):
    return render(request, 'api/register.html')
@api_view(["POST"])
def UsuarioAdd(request):
    serializer = UsuariosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return render(request, 'api/login.html')

@api_view(["GET"])
def ListarUsuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuariosSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def ValidarUsuario(request):
    
    username = request.POST["username"]
    password = request.POST["password"]
    
    data = {"username": username,"password": password}
    headers = {'Content-type': 'application/json', }
    response = requests.post('http://54.86.72.41:8000/api/v1/validar/', data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        print("Exito")
        return render(request, 'api/index.html', {'response': response})
    else:
        print("Fallo")
        