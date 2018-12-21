#!/usr/bin/python

import xmlrpclib

hosting_uri = 'https://rpc.gandi.net/xmlrpc/2.0/'
hosting_api = xmlrpclib.ServerProxy(hosting_uri)
apikey      = 'd7iDsBNAw1U3AV6UuQy7v6Hs'

print hosting_api.datacenter.list(apikey)

print hosting_api.vm.list(apikey)
print hosting_api.vm.info(apikey, 16705)

print hosting_api.vm.list(apikey, {'datacenter_id': 1})
