import Rot
import Vigenere
import hashlib


def algoritmo_descifrado():
    
    f = open("mensajeseguro.txt", "r")
    f = f.readlines()
    mensaje= f[0] #linea 0 es mensaje
    mensaje= mensaje[:-1] #borra \n
    hashOriginal = f[1] #linea 1 es hash del mensaje original

    #descifrar mensaje
    descifrando= Vigenere.descifrar_mensaje("Frita",mensaje)
    descifrando= Vigenere.descifrar_mensaje("Papa",descifrando)
    descifrando= Rot.decodificar(descifrando,4)
    #verificar si el hash es el mismo que el mensaje original
    hashNuevoMensaje = hashlib.md5(descifrando.encode()).hexdigest()

    if hashNuevoMensaje == hashOriginal:    
        print("el mensaje no esta alterado y dice:", descifrando)
    else:
        print("el mensaje esta alterado y dice:", descifrando)

algoritmo_descifrado()
