####################################################################
# Diego Sevilla 17238
####################################################################
# Curso: Redes
# Programa: main_xmpp.py
# Propósito: Menu para la interaccion con el cliente
# Fecha: 09/2020
####################################################################

# ---------------ZONA DE LIBRERIAS-------------------

#import logging
#from sleekxmpp import ClientXMPP
#from sleekxmpp.exceptions import IqError, IqTimeout

import time
import random
import string

from functions import *
#from XMPP_Client import XMPP_Registedr

import methods
#from XMPP_Client import registerUser


#! functions here -------------------------------------------------------------------
xmppclient = None

def Register():
    print("REGISTER")
    print("_______________")
    userName = input("Enter your jabberid: ")
    passWord = input("Enter a password: ")

    if(methods.registerUser(userName,passWord)):
        print()
        print('Account for '+userName+' created!')     
        print()   
    else:
        print()
        print("Couldn't create account! This account already exists!")
        print()
    pass

def Login():
    userName = input("Enter your jabberid: ")
    passW = input("pass: ")
    xclient = methods.XMPP_Client(userName,passW)
    return xclient

def Logout(xclient):
   xclient.connection_logout()

def sendPrivateMessage(xclient):
    recipient = input("Enter the JID of the person you want to message: ")
    message = input("Enter your message: ")
    xclient.sendPrivateMessage(recipient,message)

def sendRoomMessage(xclient):
    #recipient = input("Enter the JID of the person you want to message: ")
    message = input("Enter your message: ")
    xclient.sendRoomMessage(message)

def _exit(xclient):
    xclient.exit()


#! --------------------------------------------------------------------------------------------------

Wellcome()

# ciclo while para el menu del juego

def menu():
    print(" ")
    print(" -----------------------------------------------------------------")
    print("  1. Register")
    print("  2. Log In ")
    print("  3. Log Out")
    print("  4. Delete Account")
    print("  5. Show Connected users ")
    print("  6. Add user to contacts ")
    print("  7. Show Contacts and Status ")
    print("  8. Show Info from an specific user")
    print("  9. Send private message")
    print(" 10. Join chat room")
    print(" 11. Send messages to room")
    print(" . Notify Presence")
    print(" . Send/Recieve Notifications")
    print(" . Send/Recieve Files")
    print(" 12. Exit")
    print("__________________________________________________________________")

    choice = read_integer()

    if choice == 1:
        print("")
        Register()
        menu()
    elif choice == 2:
        print(" ")
        global xmppclient
        xmppclient = Login()
        menu()
    elif choice == 3:
        print(" ")
        Logout(xmppclient)
        menu()
    elif choice == 4:
        print(" ")
        xmppclient.deleteAccount()
        menu()
    elif choice == 5:
        print(" ")

        pass
    elif choice == 6:
        print(" ")

        pass
    elif choice == 7:
        print(" ")

    elif choice == 8:
        print(" ")
       

    elif choice == 9:
        print(" ")
        sendPrivateMessage(xmppclient)

    elif choice == 10:
        print(" ")

    elif choice == 11:
        print(" ")

    elif choice == 12:
        print(" ")
        theEnd()
        exit(xmppclient)

    menu()
menu()
