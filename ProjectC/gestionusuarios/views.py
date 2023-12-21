from django.shortcuts import render
from django.shortcuts import get_object_or_404
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
            return JsonResponse(data_res)
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
# here



#    def put(self, request, user_id):
#        user = get_object_or_404(Usuario, id=user_id)
#        data = json.loads(request.body)
#        user.nombre = data['nombre']
#        user.email = data['email']
#        user.edad = data['edad']
#        user.save()
#        return JsonResponse({'id': user.id, 'nombre': user.nombre, 'email': user.email, 'edad': user.edad})
#
#    def delete(self, request, user_id):
#        user = get_object_or_404(Usuario, id=user_id)
#        user.delete()
#        return JsonResponse({'message': 'Usuario eliminado correctamente'})
    
    
    #    def get(self, request, user_id=None):
#        if user_id:
#            user = get_object_or_404(Usuario, id=user_id)
#            data = {'id': user.id, 'nombre': user.nombre, 'email': user.email, 'edad': user.edad}
#        else:
#            users = Usuario.objects.all()
#            data = [{'id': user.id, 'nombre': user.nombre, 'email': user.email, 'edad': user.edad} for user in users]
#        return JsonResponse(data, safe=False)

#    def post(self, request):
#        data = json.loads(request.body)
#        usuario = Usuario.objects.create(nombre=data['nombre'], email=data['email'], edad=data['edad'])
#        return JsonResponse({'id': usuario.id, 'nombre': usuario.nombre, 'email': usuario.email, 'edad': usuario.edad})
