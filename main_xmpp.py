####################################################################
# Diego Sevilla 17238
####################################################################
# Curso: Redes
# Programa: main_xmpp.py
# Propósito: Menu para la interaccion con el cliente
# Fecha: 09/2020
####################################################################

# ---------------ZONA DE LIBRERIAS-------------------
import logging
from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout

import time
import random
import string

from functions import * 
from XMPP_Client import XMPP_Client

# functions here
#xmppclient = None

def Register():
    userName = input("Enter your jabberid: ")
    passWord = input("Enter a password: ")
    xmppclient = XMPP_Client(userName,passWord)
    return xmppclient

def sendMessage(xclient):
    recipient = input("Enter the JID of the person you want to message: ")
    message = input("Enter your message: ")
    xclient.sendMessage(recipient,message,"chat")

def _exit(xclient):
    xclient.exit()


# --------------

Wellcome()
out = 0

# ciclo while para el menu del juego
while out != 1:
    print(" ")
    print(" -----------------------------------------------------------------")
    print("  1. Register")
    print("  2. Log In (New Account)")
    print("  3. Log Out")
    print("  4. Delete Account")
    print("  5. Show Connected users, contacts and status) ")
    print("  6. Show Info from an specific user")
    print("  7. Two Persons Chat")
    print("  8. Group Chat")
    print("  9. Notify Presence")
    print(" 10. Send/Recieve Notifications")
    print(" 11. Send/Recieve Files")
    print(" 12. Exit")
    print("__________________________________________________________________")

    choice = read_integer()

    if choice == 1:
        print("")
        Register()

    elif choice == 2:
        print(" ")
        sendMessage(Register())
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print(" ")
        test = input("input something: ")
        
        pass
    elif choice == 6:
        print(" ")

        pass
    elif choice == 7:
        print(" ")
        
        pass
    elif choice == 8:
        pass
    elif choice == 9:
        pass
    elif choice == 10:
        pass
    elif choice == 11:
        pass
    elif choice == 12:
        out = 1
        theEnd()
        _exit()
