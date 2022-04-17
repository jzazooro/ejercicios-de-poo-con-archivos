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
        