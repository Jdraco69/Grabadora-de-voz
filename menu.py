import time 
from principal_graba import audio
while True :
    print("opciones:")
    print("1.grabar")
    print("2.salir")
    op=int(input("coloque su opcion:"))
    if op== 1 :
       audio_duracion=int(input("cuanto durara el audio ?"))
       print("grabando audio en ..")
       print("3") 
       print("2")
       print("1")
       audio(audio_duracion)
    elif op == 2 :
        break   
    else:
        print("opcion invalida")
