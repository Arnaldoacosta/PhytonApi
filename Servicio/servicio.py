from Modelo.model_notasMaterias import NotaMateria
from flask import jsonify
import json
from controller import Response
from flask_api import FlaskAPI, status
from Servicio.Exception_api import ApiExceptionServ,NotFound,InternalServerError
import requests
from Servicio.Errores_internos import CodeInternalError


#add notaMateria
def addNotaMateria(request): 
    notamateria=setNotaMateria(request)
    try:
        notamateria.save()
        content = {'detalle': 'Recurso creado.'}
        return content, status.HTTP_201_CREATED 
    except Exception as identifier:
        raise InternalServerError('Error relacionado con base de datos.', CodeInternalError.ERROR_INTERNO_11_CONEXION_BD)       
    
    
    '''return "Materia agregarda. id={}".format(notamateria.notamateria_id)'''

#get
def findNotasMateriasByAlumnoID(id):                 
        obj=NotaMateria.getNotasMateriasByAlumnoID(id) 
        if obj is not None and len(obj)!=0:
            json_Str=jsonify([e.serializar() for e in obj]) 
            return json_Str
        else:
            raise NotFound()
            #content = {'detalle': 'Recurso no encontrado.','cod_error_interno':'2','descripcion_error':'No se encontraron registros con los datos ingresados.'}
            #return content, status.HTTP_404_NOT_FOUND,content'''

# Get all NotasMaterias
def getNotasMaterias():
    materias=NotaMateria.buscarNotasMaterias()
    json_Str=jsonify([e.serializar() for e in materias]) 
    return json_Str

#Update
def updateNotaMateria(request):
    #raise PermissionDenied()
    try:      
        notamateria_id=request.json['notamateria_id']
        ''' alumno_id=request.json['alumno_id']'''
        nombremateria=request.json['nombremateria']
        notafinal=request.json['notafinal']  
    except Exception as e:
        return ({'detail':'Json mal formado'},status.HTTP_400_BAD_REQUEST)     
    notamateria=NotaMateria.buscarNotaMateriaByNotamateriaID(notamateria_id)
    if notamateria is None:
        content = {'detail': 'Recurso no encontrado'}
        return content, status.HTTP_404_NOT_FOUND
    else:          
        notamateria.nombremateria=nombremateria,
        notamateria.notafinal=notafinal
        notamateria.save()
        return ('Registro editado.')

# Update
def updateNotaMateriasByAlumnoID(id):
    try:      
        obj=NotaMateria.buscarMateriasByAlumnoID(id)
        json_str=jsonify([e.serializar() for e in obj])
        return (json_str)
    except Exception as e:
	    return(str(e))

#
def deleteNotaMateria(id):
    notamateria=NotaMateria.buscarNotaMateriaByNotamateriaID(id)
    notamateria.delete()
    return ('Registro eliminado') 
    '''try:
        1==1
    except Exception as e:
        return TaskNotFound(e)
    finally
        return TaskNotFound(APIException)'''
    #notamateria=NotaMateria.buscarNotaMateriaByNotamateriaID(id)
    #notamateria.delete()
    #return ('se elimino')  

#Methods
def setNotaMateria(request):
    try:   
        notamateria=NotaMateria(
            request.json['alumno_id'],
            request.json['nombremateria'],
            request.json['notafinal'] 
        )
    except Exception as identifier:
        raise NotFound('Estructa de Json incorrecta',CodeInternalError.ERROR_INTERNO_10_JSON_BAD_FORMED)
    return notamateria
       

       
def setMessajeFormatJson():
    return ({'detail':'Estructura json no soportada'},status.HTTP_400_BAD_REQUEST)
#

def imprimirJson():
    notamateria = NotaMateria('11','estadistica','10') 
    json_data = json.dumps(notamateria) 
    print (json_data)
    return (json_data)





