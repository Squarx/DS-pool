#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys
import optparse
import pandas
def callPublicFlightAPI(app_id, app_key):
    url = 'https://api.schiphol.nl/public-flights/flights'

    headers = {
      'accept': 'application/json',
	  'resourceversion': 'v4',
      'app_id': app_id,
	  'app_key': app_key
	}

    try:
        response = requests.request('GET', url, headers=headers)
    except requests.exceptions.ConnectionError as error:
        print(error)
        sys.exit()

    if response.status_code == 200:
        flightList = response.json()
        
        print('found {} flights.'.format(len(flightList['flights'])))
       
        for flight in flightList['flights']:
            print('Found flight with name: {} scheduled on: {} at {}'.format(
                flight['flightName'],
                flight['scheduleDate'],
                flight['scheduleTime']))
            
    else:
        print('''Oops something went wrong
Http response code: {}
{}'''.format(response.status_code,
             response.text))
    for i in list(flightList['flights'][0].keys()):
            print("{:<30}{}".format(i[:15], flightList['flights'][0][i]))

if __name__ == '__main__':
    callPublicFlightAPI(app_id='1f180f30', app_key='95c479567454a8896b434f1251e0938c')
