# ejercicios-de-poo-con-archivos

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/ejercicios-de-poo-con-archivos.git)

He realizado tres ejercicios a cerca de las calificaciones de los alumnos de una clase que formaban parte de un archivo.csv

### Ejercicio1

```
def nota(numero):
    numero=numero.replace(',','.')
    return float (numero)

def calificaciones(sumatorio):
    try:
        f=open(sumatorio, 'r')
    except FileNotFoundError:
        print("no se ha encontrado el fichero seleccionado")
        return
    lecturadelista = f.readlecturadelista()
    f.close()
    comando=lecturadelista[0][:-1].split(";")
    calificaciones=[]
    for i in lecturadelista[1:]:
        valor=i[:-1].split(";")
        alumno={}
        for j in range(len(valor)):
            alumno[comando[j]]=valor[j]
            calificaciones.append(alumno)
    return calificaciones
```

### Ejercicio2

```
from clases.ejercicio1 import *
def notafinalalumno(calificaciones):
    def notafinal(alumno):
        if alumno['ordinario 1']:
            parcialuno=nota(alumno['ordinario 1'])
        elif alumno['parcial 1']:
            parcialuno=nota(alumno['parcial 1'])
        else:
            parcialuno=0
        if alumno['ordinario 2']:
            parcialdos=nota(alumno['ordinario 2'])
        elif alumno['parcial 2']:
            parcialdos=nota(alumno['parcial 2'])
        else:
            parcialdos=0
        if alumno['practicaordinaria']:
            practicas=nota(alumno['practicaordinaria'])
        elif alumno['practica']:
            practicas=nota(alumno['practicas'])
        else:
            practicas=0
        
        alumno['final1']=parcialuno
        alumno['final2']=parcialdos
        alumno['finalpracticas']=practicas
        alumno['notafinal']=parcialuno*0.3 + parcialdos*0.3 + practicas*0.4
        return alumno

    return list(map(notafinal, calificaciones))
```

### Ejercicio3

```
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
```
