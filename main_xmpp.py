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
#from XMPP_Client import XMPP_Register

import metodos
#from XMPP_Client import registerUser


#! functions here -------------------------------------------------------------------


def Register():
    print("REGISTER")
    print("_______________")
    userName = input("Enter your jabberid: ")
    passWord = input("Enter a password: ")
    
    if(metodos.registerUser(userName,passWord)):
        print('yes')        
    else:
        print('no')
    pass

def Login():
    #xclient.sendMessage(recipient,message,"chat")
    userName = input("Enter your jabberid: ")
    passW = input("pass: ")
    xclient = metodos.XMPP_Client(userName,passW)
    return xclient

def Logout(xclient):
   ''' xclient.connection_logout()'''

def sendMessage(xclient):
    '''recipient = input("Enter the JID of the person you want to message: ")
    message = input("Enter your message: ")
    xclient.sendMessage(recipient,message,"chat")'''

def _exit(xclient):
    xclient.exit()


#! --------------------------------------------------------------------------------------------------

Wellcome()
out = 0
xmppclient = None
# ciclo while para el menu del juego
while out != 1:

    print(" ")
    print(" -----------------------------------------------------------------")
    print("  1. Register")
    print("  2. Log In ")
    print("  3. Log Out")
    print("  4. Delete Account")
    print("  5. Show Connected users, contacts and status) ")
    print("  6. Show Info from an specific user")
    print("  7. Two Persons Chat")
    print("  8. Group Chat")
    print(" . Notify Presence")
    print(" . Send/Recieve Notifications")
    print(" . Send/Recieve Files")
    print(" 9. Exit")
    print("__________________________________________________________________")

    choice = read_integer()

    if choice == 1:
        print("")
        Register()

    elif choice == 2:
        print(" ")
        global xmppclient
        xmppclient = Login()

    elif choice == 3:
        Logout(xmppclient)
        pass
    elif choice == 4:
        userName = input("user: " )
        xmppclient.deleteAccount(userName)
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
        sendMessage(xmppclient)
        
    elif choice == 8:
        pass
    elif choice == 9:
        out = 1
        theEnd()
        exit(xmppclient)
