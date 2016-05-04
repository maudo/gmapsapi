import googlemaps
import sqlite3
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyAHxfXJErx1yQxv5otuj3Y7nrxKkD5paGY')

sIn = raw_input("Enter source: ")
dIn = raw_input("Enter destination: ")

def getDirections(source, destination):
    badInput = False

    sPl = gmaps.places(source)
    if (str(sPl[u'status']) == "ZERO_RESULTS"):
        print "Bad Source"
        badInput = True
    else:
        src = str(sPl[u'results'][0][u'formatted_address'])

    dPl = gmaps.places(destination)
    if (str(dPl[u'status']) == "ZERO_RESULTS"):
        print "Bad Destination"
        badInput = True
    else:
        dst = str(dPl[u'results'][0][u'formatted_address'])

    if badInput:
        return

    dirs = gmaps.directions(src, dst, departure_time=datetime.now())
    dirsInfo = dirs[0][u'legs'][0]

    time = dirsInfo[u'duration_in_traffic'][u'value']
    dist = dirsInfo[u'distance'][u'value']

    if (time < 60):
        tNew = str(time) + " seconds"
    elif (time < 60 * 60):
        tNew = str(round(time / 60.0, 2)) + " minutes"
    elif (time < 60 * 60 * 24):
        tNew = str(round(time / 60.0 / 60.0, 2)) + " hours"
    else:
        tNew = str(round(time / 60.0 / 60.0 / 24.0, 2)) + " days"

    dNew = str(round(0.000621371 * dist, 2)) + " miles"

    print "Source: " + src
    print "Destination: " + dst
    print "t = " + tNew
    print "d = " + dNew

getDirections(sIn, dIn)
