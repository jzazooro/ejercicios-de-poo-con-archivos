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
