import Rot
import Vigenere
import hashlib


def algoritmo_cifrado():
    #abrir input
    f = open("mensajedeentrada.txt", "r")
    f = f.read()
    hash_value = hashlib.md5(f.encode()).hexdigest()
    
    #cifrar mensaje
    cifrando= Rot.codificar(f,4)
    cifrando= Vigenere.cifrar_mensaje("Papa",cifrando)
    cifrando= Vigenere.cifrar_mensaje("Frita",cifrando)

    print("El mensaje codificado es:",cifrando)
    print("El hash del mensaje original es:",hash_value)
    #generar archivo, escribir mensaje y hash
    output= open("mensajeseguro.txt","w+") 
    output.write(cifrando +'\n'+hash_value) 
    output.close()

algoritmo_cifrado()