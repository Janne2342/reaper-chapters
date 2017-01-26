#!/usr/bin/python

# -*- coding: utf-8 -*-
# A comment to commit
#total kaputt
import sys

def zeilen(zeile):
    if "\r\n" in zeile:
        zeile = zeile.replace('\r\n','')
    #while zeile[-1] == ' ':
        #zeile = zeile[:-1]
    zeile = zeile.strip(' ')

    time = zeile[-12:]
    #print time    
    if time[3] == ' ':
        time = '00:0' + time[4:]
    if time[2] == ' ':
        time = '00:' + time[3:]
    if time[0] == ' ':
        time = '0' + time[1:]    
    #print time
    titel = zeile[2:-15]
    #while titel[0] == ' ':
        #titel = titel[1:]
    titel = titel.strip(' ')
    
    #print titel
    neue_zeile = time + ' ' + titel + '\r\n'
    #print neue_zeile
    return(neue_zeile)

if len(sys.argv) < 2:
    print 'Please attach a file.'
    sys.exit()
if len(sys.argv) > 2:
    print 'Please attach only ONE file.'
    sys.exit()
try:
    open(sys.argv[1],"r")
except IOError:
    print('File not found.')
    sys.exit()    
    
filename = sys.argv[1]
file_alt = open(filename,"r") 
alte_liste = file_alt.readlines()
file_alt.close
#print liste
alte_liste.remove(alte_liste[0])
alte_liste.remove(alte_liste[0])
neue_liste = []

for zeile in alte_liste:
    #print zeile
    neue_zeile = zeilen(zeile)
    #print neue_zeile    
    neue_liste.append(neue_zeile)
    
        
#print neue_liste[6]
filename_neu = filename[:filename.find('markers')] + 'chapters.txt'
#print filename_neu
file_neu = open(filename_neu,"w")
file_neu.writelines(neue_liste)
file_neu.close
