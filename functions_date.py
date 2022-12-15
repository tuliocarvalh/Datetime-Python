from datetime import datetime
import time


def agora() :
    agora = datetime.now()
    return agora
    
def hora() :
    agora = datetime.now()
    hora = agora.hour
    return hora

def minuto() :
    agora = datetime.now()
    minuto = agora.minute
    return minuto

def mes() :
    mes = datetime.today().strftime('%m')
    return mes
    
def dia() :
    dia = datetime.today().strftime('%d')
    return dia    


