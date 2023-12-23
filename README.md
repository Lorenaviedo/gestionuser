# Python Prueba Andes

A continuación, le presento la aplicación solicitada, detallando cada punto junto con su respectiva descripción. 

Se desarrollo una aplicación para el registro de usuarios de la compañía Andes SCD, permitiendo realizar operaciones como leer, agregar, actualizar y eliminar. 


## Tech Stack



Herramientas y Tecnologías Utilizadas: 

  

Backend:  Python-Django:  

  

Frontend: React 
## 🔗 Links
https://github.com/polodiaz/Andesprueba.git


## Documentation

1) Configuración de la Base de Datos:
   - Importante configuracion de datos en Mysql server

Crea una base de datos MySQL llamada usuarios_andes 

  
```bash
Solución: 

Se procedió a crear en Mysql una base de Datos llamada usuarios_andes. 
Utilizano el siguiente comando CREATE DATABASE usuarios_andes; se adjunta Ejemplo.

create DATABASE usuarios_andes;
```
 



2:  ¿Dentro de la base de datos, crea una tabla usuarios con los siguientes campos:? 



id (clave primaria, autoincremento) 



nombre,email,Edad 

 
```bash

Solucion:
Utilizando el siguiente comando CREATE TABLE usuarios; 
 
CREATE TABLE usuarios( 

    id INT AUTO_INCREMENT PRIMARY KEY, 

    nombre VARCHAR(255), 

    email VARCHAR(255), 

    edad INT 

); 
  
```



3.

Modelo de Usuario: 

¿Crea un modelo Usuario que represente a la tabla usuarios en la base de datos.? 
 

 bash
 Solucion:  
 

Se procede a la creación del modelo utilizando los siguientes comandos, creando una clase con los campos solicitados, los cuales coinciden con la información de la base de datos: 

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

  


4.

Operaciones CRUD: 

 
Crear: ¿ Escribe una función que permita agregar un nuevo usuario a la base de datos. ? 

 
 
bash
Solución: 
 
  Se procede con la función Post, dentro un bloque Try la cual intenta la ejecución del código respectivo y el caso hipotético de una excepción se ejecuta el except , a continuación, imagen alusiva. 

def post(self,request):
        try:
            jsondatos = json.loads(request.body)
            usuario = Usuario(nombre=jsondatos['nombre'], email=jsondatos['email'], edad=jsondatos['edad'])
            usuario.save()
            datos = {
                'mensaje': "Exitoso"
            }
            
        except json.JSONDecodeError as  error:
            print(f'json decode error:{error}')
            datos = {'mensaje':"solicitud de JSON Invalida"}
        return JsonResponse(datos)
  


 5.
 Leer: ¿ Escribe una función para leer los datos de un usuario específico o de todos los usuarios. ?  

 
 
bash

Solucion: 
 
La creación de la función GET está en marcha, y se propone que solo se pueda filtrar por un ID identificador único. Esta propuesta tiene como objetivo simplificar el filtro, ya que la búsqueda se centra en un dato único, siendo el ID el elemento que no se duplica. 

def get(self,request, id=0):
        if (id > 0):
            usuarios = list(Usuario.objects.filter(id=id).values())
            if len(usuarios) > 0:
                usuario = usuarios[0]
                datos = {'mensaje': "Exito", 'usuario': usuario}
                return JsonResponse(datos)
        else:
            usuarios = list(Usuario.objects.values())
            if len(usuarios) > 0:
                datos = {'mensaje': "Exito", 'usuarios': usuarios}
                return JsonResponse(datos)
  


6.

Actualizar: ¿ Escribe una función que actualice los datos de un usuario existente. ? 

 


bash
Solución: 

 

Se procede con la creación de la función PUT la cual obtiene los datos de Usuario el cual es el modelo y se filtra por el ID y cuando la longitud es mayor a 0 la actualiza.


    def put(self,request, id):
        jsondatos = json.loads(request.body)
        usuarios = list(Usuario.objects.filter(id=id).values())
        if len(usuarios)> 0:
            usuario = Usuario.objects.get(id=id)
            usuario.nombre = jsondatos['nombre']
            usuario.email = jsondatos['email']
            usuario.edad = jsondatos['edad']
            usuario.save()
            datos = {'mensaje': "Exito en la actualizacion"}
    
        else:
            datos = {'mensaje': "error en la actualizacion"}
        return JsonResponse(datos)

  



7.  Eliminar: ¿ Escribe una función que permita eliminar un usuario de la base de datos. ? 

 

 
bash
Solución: 

Se procede con la creación de la función delete la cual obtiene los datos de Usuario el cual es el modelo y se filtra por el ID y cuando la longitud es mayor a 0 la elimina se utiliza el método delete que trae Django por defecto.


 def delete(self,request, id):
        usuarios=list(Usuario.objects.filter(id=id).values())
        if len(usuarios)>0:
            Usuario.objects.filter(id=id).delete()
            datos = {'mensaje': "Exito en la eliminacion"}
            
        else:
            datos = {'mensaje': "error en la eliminacion"}
        return JsonResponse(datos)
  

8. Rutas y Vistas: 

urlpatterns = [
    - /usuario/: maneja las operaciones GET y POST que obtienen la lista de usuarios o crean un nuevo usuario
    path('usuarios/', UsuarioView.as_view(), name='Listar Usuarios'),
    - /usuario/id/: maneja las operaciones GET, PUT, DELETE, las cuales obtienen, actualizan y eliminan un usuario específico según su ID
    path('usuarios/<int:id>/', UsuarioView.as_view(), name='User Detail by ID'),
]

## 1. Informacion FRONTEND - React
Para el front de la aplicacion "gestion de usuarios" se genero por medio de React 
## 1.1. Herramientas para React 

- se implemento la Herramienta Vite para el manejo de React
- Importante! --> INSTALACION DE REACT
- Instalaciones: 

```bash
  npm create vite
  cd client -- ingresar al directorio creado
  npm install -- instalacion de paquetes
  npm run dev -- correr el front

  react-router-dom --> Biblioteca utilizada para gestionar múltiples rutas en la aplicación.
  react-hot-toast --> Biblioteca empleada para mostrar notificaciones cuando se realizan cambios en la aplicación web.
  axios --> Librería utilizada para realizar peticiones HTTP desde el cliente.
  react-hook-form --> Utilizado para facilitar el manejo y recolección de datos mediante formularios en React.
```
## 1.2. CRUD
Se realizaron las peticiones para el Backend por medio de la libreria Axios, creando una baseURL a nuestra ruta "http://127.0.0.1:8000/api/usuarios/" para las cuatro peticiones:
- Get
```bash
import axios from 'axios'

const usuarioApi = axios.create({
    baseURL: "http://127.0.0.1:8000/api/usuarios/",
})
export const getUsuarios = () => usuarioApi.get("/");
```
- Put
- Post
- Delete

## Authors

- [@cristian.diaz](https://github.com/polodiaz)
