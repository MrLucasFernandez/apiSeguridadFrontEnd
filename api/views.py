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
import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL","https://hedwmixgqtmxzppsucbn.supabase.co")
key: str = os.environ.get("SUPABASE_KEY","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhlZHdtaXhncXRteHpwcHN1Y2JuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTc3NzI1MDMsImV4cCI6MjAzMzM0ODUwM30.f9vEpMtNGIFU7xO11w51Ct9CDVFY78RndNnNg_ntseI")
supabase: Client = create_client(url, key)


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
    
    
    response = supabase.table('api_usuario').select("*").eq('username', 'admins',).eq('password', 'pbkdf2_sha256$600000$9sDL2XFqPjtgWltvCXjjGb$5JW6Fq0aMlWKYdzzQA0kUV+1BcnBPzvlcCtIyXYGBb8=').execute()
    if response != '':
        return HttpResponse(response.json())
    else:
        return HttpResponse("Credenciales inválidas")

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
        