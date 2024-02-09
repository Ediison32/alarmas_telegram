

# configuracion de tiempo 

import datetime


def fechaActual():
    fecha_hora_actual = datetime.datetime.now()
    format = "%d-%m-%Y  %H:%M"
    fecha_hora_formateada = fecha_hora_actual.strftime(format)
    hora = datetime.datetime.now().time().hour
    minuto = datetime.datetime.now().time().minute
    return fecha_hora_formateada, hora, minuto
