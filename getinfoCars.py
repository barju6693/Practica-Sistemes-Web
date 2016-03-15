#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Sergi Cervera
'''
from edmunds import Edmunds
import pprint
import sys
import requests
import json

api = Edmunds('api_key')

# URL EXAMPLE : {protocol}://api.edmunds.com/{endpoint}?fmt={response format}&api_key={API key}

url_base = "://api.edmunds.com/"
url_protocol = {"http": "http",
                "https": "https"
                }
endpoint = {}
response_format = "json"
api_key = ""


def car():
    # r = api.make_call('/api/vehicle/v2/makes')
    # print r
    """response = api.make_call('/api/vehicle/v2/lexus/rx350/2011/styles')
    pprint.pprint(response)"""

    response = api.make_call('/api/vehicle/v2/makes')
    pprint.pprint(response)
    print "A"
    #r = requests.get("https://api.edmunds.com/api/vehicle/v2/makes?fmt=json&api_key=3ftdty95p7uta5qqy8gfgq2y")
    # r = requests.get("https://api.edmunds.com/api/vehicle/v2/honda/models?year=2001&fmt=json&api_key=3ftdty95p7uta5qqy8gfgq2y")
    #jsondata = json.loads(r.text)
    #pprint.pprint(jsondata)
    # print jsondata


if __name__ == "__main__":
    car()
