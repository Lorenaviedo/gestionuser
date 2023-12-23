from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Usuario
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json


class UsuarioView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #csrf_exempt es un decorador que desactiva la protección contra ataques CSRF 
    # (Cross-Site Request Forgery) para la vista específica.
    
    # This work successfully
    def get(self, request, id=0):
        if (id>0):
            users = list(Usuario.objects.filter(id=id).values())
            if len(users) > 0:
                user = users[0]
                data_res = {'message': "Success", 'user':user }
            else:
                data_res = {'message': "user not found..."}
            #return JsonResponse(data_res)
        else:
            users = list(Usuario.objects.values()) # Convert QuerySet to list of dictionaries
            if len(users) > 0:
                data_res = {'message': "Success", 'users':users }
            else:
                data_res = {'message': "users not found..."}
        
        return JsonResponse(data_res)
    
    
    def post(self, request):
        try:
            jdata = json.loads(request.body)
            user = Usuario(nombre=jdata['nombre'], email=jdata['email'], edad=jdata['edad'])
            user.save()
            data_res = {'message': "Success"}
        except json.JSONDecodeError as error:
            print(f'JSON Decode Error: {error}') 
            data_res = {'message': "Invalid JSON in request body (structure or fault)"}
            
        return JsonResponse(data_res)
    
    
    def put(self, request, id):
        jdata = json.loads(request.body)
        users = list(Usuario.objects.filter(id=id).values())
        if len(users) > 0:
            user = Usuario.objects.get(id=id)
            user.nombre = jdata['nombre']
            user.email = jdata['email']
            user.edad = jdata['edad']
            user.save()
            data_res = {'message': "Success"}
        else:
            data_res = {'message': "Error 404 User not Found..."}
        
        return JsonResponse(data_res)
    
    
    def delete(self, request, id):
        users = list(Usuario.objects.filter(id=id).values())
        if len(users)>0:
            Usuario.objects.filter(id=id).delete()
            data_res = {'message': "Success"}
        else:
            data_res = {'error': "e404 User not Found..."}
            
        return JsonResponse(data_res)

# views
def home(request):
    return HttpResponse("<h2>Welcome to my app</h2>")
