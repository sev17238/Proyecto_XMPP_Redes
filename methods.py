#!/usr/bin/env python
# -*- coding: utf-8 -*-

####################################################################
# Diego Sevilla 17238
####################################################################
# Curso: Redes
# Programa: methods.py
# Propósito: module with a registerFunction and a xmpp client class
# for interacting with a xmpp server.
# Fecha: 08/2020
####################################################################


"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2010  Nathanael C. Fritz
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

import sys
import logging
import getpass
from optparse import OptionParser

import sleekxmpp
from sleekxmpp.exceptions import IqError, IqTimeout
import xmpp
import threading
import xml.etree.ElementTree as TreeX

# Python versions before 3.0 do not use UTF-8 encoding
# by default. To ensure that Unicode is handled properly
# throughout SleekXMPP, we will set the default encoding
# ourselves to UTF-8.
if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    raw_input = input

def registerUser(user,passw):
    usuario = user
    password = passw
    jid = xmpp.JID(usuario)
    cli = xmpp.Client(jid.getDomain(), debug=[])
    cli.connect()
    if xmpp.features.register(cli, jid.getDomain(), {'username': jid.getNode(), 'password': password}):
        return True
    else:
        return False

class XMPP_Client(sleekxmpp.ClientXMPP):
    """
    A XMPP client that will have an account
    with an XMPP server and interact with it respectively.
    """
    def __init__(self, jid, password):
        #sleekxmpp.ClientXMPP.__init__(self, jid, password)
        #super(XMPP_Client, self).__init__(jid, password)
        sleekxmpp.ClientXMPP.__init__(self, jid, password)

        self.connected = True
        self.auto_authorize = True 
        self.auto_subscribe = True 
        self.jabberid = jid

        #self.room = None

        self.add_event_handler('session_start', self.session_start)
        self.add_event_handler("message", self.receive_messages)
        #self.add_event_handler("changed_subscription", self.getRosterFor)
        self.add_event_handler("got_offline",self.offline_notification)

        self.presences_received = threading.Event()
        #self.add_event_handler("got_online",self.online_notification)

        self.received_list = set()
        self.contacts = []
        self.users_list = {}
        self.contacts_list = {}
        self.username = jid
        #self.recieved_presences = threading.Event()
        
        self.register_plugin('xep_0030') # Service Discovery
        self.register_plugin('xep_0004') # Data forms
        self.register_plugin('xep_0066') # Out-of-band Data
        self.register_plugin('xep_0077') # In-band Registration
        self.register_plugin('xep_0096') # Jabber search
        self.register_plugin('xep_0199') # XMPP Ping

        '''self.plugin['xep_0045'].joinMUC(self.room,
                                        self.nick,
                                        # If a room password is needed, use:
                                        # password=the_room_password,
                                        wait=True)'''

        if self.connect():
            print("Login Successfully! Proceed to other options.")
            self.process(block=False)
        else:
            print("Unable to connect.")


    #! Conection managment AREA --------------------------------------------------------------------------------------
    def session_start(self,event):
        """
        Start
        """
        self.send_presence(
            pshow='chat',
            pstatus='Available'
        )
        self.get_roster()

    def connection_logout(self):
        print('Logout request completed.')
        self.disconnect(wait=False)

    def exit(self):
        self.disconnect(wait=True)
        self.process(block=True)

    def deleteAccount(self):
        stanzaReq = self.Iq()
        stanzaReq['type'] = 'set'
        stanzaReq['from'] = self.jabberid
        stanzaReq['register']['remove'] = True
        try:
            stanzaReq.send(now=True)
            print("Account "+str(self.jabberid)+" deleted!")
        except IqError as e:
            logging.error("Could not delete account")
            sys.exit(1)
        except IqTimeout:
            logging.error("No response from server.")
    #! END Conection managment AREA--------------------------------------------------------------------------------------



    #! messages area --------------------------------------------------------------------------------------
    def sendPrivateMessage(self, recipient, msg):
        self.sendNotification(recipient,'Is writing...','composing')
        self.send_message(mto=recipient,
                          mbody=msg,
                          mtype='chat')

    def receive_messages(self, msg):
        print("")
        print(""+str(msg['from'].user)+"@"+str(msg['from'].domain)+": "+str(msg['body']))

    def sendRoomMessage(self, room, msg):
        self.send_message(mto=room,mbody=msg,mtype='groupchat')
   
    #! END messages area --------------------------------------------------------------------------------------
    
    def joinRoom(self,room):
        self.get_roster()
        self.send_presence()
        self.plugin['xep_0045'].joinMUC(room,
                                        self.jid,
                                        # If a room password is needed, use:
                                        # password=the_room_password,
                                        wait=True)

    #! Notifications AREA --------------------------------------------------------------------------------------
    def online_notification(self,event):
            #msg = self.sendMessage()
        #print(f"Offline Notification from {event["form"].user}")
        pass

    def offline_notification(self,event):
        print("")
        print("Offline Notification from"+ str(event["form"].user))
        print("")

    def sendNotification(self,to,body,ntype):
        msg = self.Message()
        msg['to'] = 'chat'
        msg['type'] = body
        if(ntype == 'active'): itemXML = TreeX.fromstring("<active xmlns='http://habber.org/protocol/chatstates'/>")
        elif(ntype == 'composing'): itemXML = TreeX.fromstring("<composing xmlns='http://habber.org/protocol/chatstates'/>")
        elif(ntype == 'inactive'): itemXML = TreeX.fromstring("<inactive xmlns='http://habber.org/protocol/chatstates'/>")

        msg.append(itemXML)
        try:
            msg.send()
        except IqError:
            raise Exception("Unable to send notification",IqError)
            sys.exit(1)
        except IqTimeout:
            raise Exception("Server Not Responding")


    #! Notifications AREA --------------------------------------------------------------------------------------

    #! Contacts and users area ------------------------------------------------------------------------
    def addUser(self,user):
        try:
            self.send_presence_subscription(pto=user)
            print(" "+user+" added to your contacts !")
            return 1
        except IqError:
            raise Exception("Unable to add "+user+"you your contacts. Try again.")
        except IqTimeout:
            raise Exception("Server not esponding.")

    def alert(self):
        self.get_roster()
        print(self.get_roster)

    #! Contacts and users area ------------------------------------------------------------------------

    


'''
if __name__ == '__main__':
    # Setup the command line arguments.
    optp = OptionParser()
    # Output verbosity options.
    optp.add_option('-q', '--quiet', help='set logging to ERROR',
                    action='store_const', dest='loglevel',
                    const=logging.ERROR, default=logging.INFO)
    optp.add_option('-d', '--debug', help='set logging to DEBUG',
                    action='store_const', dest='loglevel',
                    const=logging.DEBUG, default=logging.INFO)
    optp.add_option('-v', '--verbose', help='set logging to COMM',
                    action='store_const', dest='loglevel',
                    const=5, default=logging.INFO)
    # JID and password options.
    optp.add_option("-j", "--jid", dest="jid",
                    help="JID to use")
    optp.add_option("-p", "--password", dest="password",
                    help="password to use")
    optp.add_option("-t", "--to", dest="to",
                    help="JID to send the message to")
    optp.add_option("-m", "--message", dest="message",
                    help="message to send")
    opts, args = optp.parse_args()
    # Setup logging.
    logging.basicConfig(level=opts.loglevel,
                        format='%(levelname)-8s %(message)s')
    if opts.jid is None:
        opts.jid = raw_input("Username: ")
    if opts.password is None:
        opts.password = getpass.getpass("Password: ")
    if opts.to is None:
        opts.to = raw_input("Send To: ")
    if opts.message is None:
        opts.message = raw_input("Message: ")
    # Setup the XMPP_Client and register plugins. Note that while plugins may
    # have interdependencies, the order in which you register them does
    # not matter.
    #xmpp = XMPP_Client(opts.jid, opts.password)
'''