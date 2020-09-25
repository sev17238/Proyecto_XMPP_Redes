def showContactsList(self):
    try:
        self.get_roster()
    except IqError as e:
        print('Error: %s' % e.iq['error']['condition'])
    except IqTimeout:
        print('No response from server.')
    groups = self.client_roster.groups()
    for group in groups:
        print('\n%s' % group)
        print('-' * 50)
        for jid in groups[group]:
            sub = self.client_roster[jid]['subscription']
            name = self.client_roster[jid]['name']
            if self.client_roster[jid]['name']:
                print(' %s (%s) [%s]' % (name, jid, sub))
            else:
                print(' %s [%s]' % (jid, sub))
            connections = self.client_roster.presence(jid)
            for res, pres in connections.items():
                show = 'available'
                if pres['status']:
                    print('       %s' % pres['status'])