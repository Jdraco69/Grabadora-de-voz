import time 
from principal_graba import audio
# menu para grabar audio
while True :
    print("opciones:")
    print("1.grabar")
    print("2.salir")
    op=int(input("coloque su opcion:"))
    if op== 1 :
        #seleccionar duracion del audio
       audio_duracion=int(input("cuanto durara el audio ?"))
       
       print("grabando audio en ..")
       time.sleep(1)
       print("3") 
       time.sleep(1)
       print("2")
       time.sleep(1)
       print("1")
       
       print("listo para grabar")
       time.sleep(1)
       audio(audio_duracion)
    elif op == 2 :
        break   
    else:
        print("opcion invalida")
