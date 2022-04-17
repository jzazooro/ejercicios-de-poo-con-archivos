from clases.ejercicio1 import *
from clases.ejercicio2 import *

def alumnosaprobadosysuspensos(calificaciones):
    aprobados=[]
    suspensos=[]
    for alumno in calificaciones:
        if all([int(alumno['asistencia'][:-1])>=75 , alumno['finaluno']>=4 , alumno['practicas']>=4 , alumno['notafinal']=5]):
            aprobados.append(alumno['apellido'] + ',' + alumno['nombre'])
        else:
            suspensos.append(alumno['apellidos'] + ',' + ['nombre'])
        return aprobados
        return suspensos
print(notafinalalumno(calificaciones('calificaciones.csv')))
aprobados , suspensos = alumnosaprobadosysuspensos(notafinalalumno(calificaciones('calificaciones.csv')))
print('la lista de aprobados es: ' , aprobados)
print('la lista de suspensos es: ' , suspensos)