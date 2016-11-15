import urllib.request
import json
from pprint import pprint

def response_to_coord(response):
    """Returns latitude and longitude as a list when given the JSON response of a Google Maps API geocode query"""
    coord = []
    coord.append(response['results'][0]['geometry']['location']['lat'])
    coord.append(response['results'][0]['geometry']['location']['lng'])
    return coord

def JSON_response(url):
    """Takes a url and gets the response in JSON format"""
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    return json.loads(response_text)

def google_url(address):
    """Returns a Google Maps API geocode request url from an address or place name"""
    params = address.replace(' ', '+')
    return 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyCf8_TxB2ELtA2kgDQZoVmZJHZZaufoK5w' %(params)

def mbta_url(coord):
    """Returns a MBTA API request url from a set of coordinates"""
    return 'http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=vSPU1c7EtEiU-JKg1C5dWA&lat=%s&lon=%s&format=json' %(coord[0], coord[1])

def get_stops(address):
    """Returns the response of a stopsbylocation query using the coordinates from a given address"""
    goog_response = JSON_response(google_url(address))
    coordinates = response_to_coord(goog_response)
    mbta_response = JSON_response(mbta_url(coordinates))
    return mbta_response

def print_stop(address):
    """Prints the nearest stop to a given address"""
    try:
        mbta_response = get_stops(address)
        stop_name = mbta_response['stop'][0]['stop_name']
        distance = float(mbta_response['stop'][0]['distance'])
        answer = [stop_name, distance]
        return answer
    except IndexError:
        return None

def main():
    print_stop('Harvard University')

if __name__ == '__main__':
    main()