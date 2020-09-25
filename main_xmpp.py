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
currentroom = ''

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

def deleteAccount(xclient):
    xclient.deleteAccount()

def sendPrivateMessage(xclient):
    recipient = input("Enter the JID of the person you want to message: ")
    message = input("Enter your message: ")
    xclient.sendPrivateMessage(recipient,message)

def joinRoom(xclient):
    #recipient = input("Enter the JID of the person you want to message: ")
    room = input("Enter the name of the room: ")
    xclient.joinRoom(room)
    return room

def sendRoomMessage(xclient,room):
    #recipient = input("Enter the JID of the person you want to message: ")
    message = input("Enter your message: ")
    xclient.sendRoomMessage(room,message)

def addUser(xclient):
    user = input("Enter the user you want to add to your contacts: ")
    xclient.addUser(user)

def usersList(xclient):
    #xclient.alert()
    xclient.serverResponseList()

def showContacts(xclient):
    xclient.showContactsList()

def checkUser(xclient,user):
    user = input("Enter a user: ")
    xclient.checkUser(user)

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
        deleteAccount(xmppclient)
        menu()
    elif choice == 5:
        print(" ")
        usersList(xmppclient)
        menu()
    elif choice == 6:
        print(" ")
        addUser(xmppclient)
        menu()
    elif choice == 7:
        print(" ")
        showContacts(xmppclient)
    elif choice == 8:
        print(" ")
        checkUser(xmppclient)
    elif choice == 9:
        print(" ")
        sendPrivateMessage(xmppclient)
        menu()
    elif choice == 10:
        print(" ")
        currentroom = joinRoom(xmppclient)
        menu()
    elif choice == 11:
        print(" ")
        sendRoomMessage(currentroom,xmppclient)
        menu()
    elif choice == 12:
        print(" ")
        theEnd()
        exit(xmppclient)

    menu()

menu()

