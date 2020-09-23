#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

# Python versions before 3.0 do not use UTF-8 encoding
# by default. To ensure that Unicode is handled properly
# throughout SleekXMPP, we will set the default encoding
# ourselves to UTF-8.
if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    raw_input = input


class XMPP_Client(sleekxmpp.ClientXMPP):
    """
    A XMPP client that will attempt to register an account
    with an XMPP server and interact with it respectively.
    """
    def __init__(self, jid, password):
        #sleekxmpp.ClientXMPP.__init__(self, jid, password)
        super(XMPP_Client, self).__init__(jid, password)

        self.auto_authorize = True 
        self.auto_subscribe = True 

        self.add_event_handler("session_start", self.start) # The session_start event will be triggered when the connection with the server and the XML streams are ready for use.        
        self.add_event_handler("register_user", self.register) # The register event provides an Iq result stanza with a registration form from the server.
        self.add_event_handler("receive_messages", self.receive_messages)
        #self.add_event_handler("sendMessage", self.sendMessage)
        self.add_event_handler("offline",self.offline_notification)

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

        if self.connect():
            print("Login Successfully!")
            self.process(block=False)
        else:
            print("Unable to connect.")


    def start(self, event):
        """
        Process the session_start event.
        Typical actions for the session_start event are
        requesting the roster and broadcasting an initial
        presence stanza.
        """
        self.send_presence(
            pshow='chat',
            pstatus='Available'
        )
        self.get_roster(
        )

    def register(self, iq):
        """
        Fill out and submit a registration form.
        The form may be composed of basic registration fields, a data form,
        an out-of-band link, or any combination thereof. Data forms and OOB
        links can be checked for as so:
        """
        resp = self.Iq()
        resp['type'] = 'set'
        resp['register_user']['username'] = self.boundjid.user
        resp['register_user']['password'] = self.password

        try:
            resp.send(now=True)
            logging.info("Account created for %s!" % self.boundjid)
        except IqError as e:
            logging.error("Could not register account: %s" %
                    e.iq['error']['text'])
            self.disconnect()
        except IqTimeout:
            logging.error("No response from server.")
            self.disconnect()

    def sendMessage(self, recipient, msg, m_type):
        self.send_presence()
        self.get_roster()

        self.send_message(mto=recipient,
                          mbody=msg,
                          mtype=m_type)

    def offline_notification(self,event):
        print("hi")
        #print(f"Offline Notification from {event["form"].user}")

    def receive_messages(self, event, recipient, msg):
        self.send_presence()
        self.get_roster()

        #self.send_message(mto=recipient,
        #                  mbody=msg,
        #                  mtype='chat')

    def exit(self):
        self.disconnect(wait=True)


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