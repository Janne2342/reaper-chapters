#!/usr/bin/python

# -*- coding: utf-8 -*-

import sys

def zeilen(zeile):
    if "\r\n" in zeile:
        zeile = zeile.replace('\r\n','')
    while zeile[-1] == ' ':
        zeile = zeile[:-1]

    time = zeile[-12:]
    #print time    
    if time[3] == ' ':
        time = '00:0' + time[4:]
    if time[2] == ' ':
        time = '00:' + time[3:]
    if time[0] == ' ':
        time = '0' + time[1:]    
    #print time
    titel = zeile[4:-15]
    while titel[0] == ' ':
        titel = titel[1:]
    
    #print titel
    neue_zeile = time + ' ' + titel + '\r\n'
    #print neue_zeile
    return(neue_zeile)
    
filename = sys.argv[1]
file_alt = open(filename,"r") 
alte_liste = file_alt.readlines()
file_alt.close
#print alte_liste
length = len(alte_liste)
i = 2
neue_liste = []
while i < length:
    #print alte_liste[i]
    neue_zeile = zeilen(alte_liste[i])
    #print neue_zeile    
    neue_liste.append(neue_zeile)
    i = i + 1
        
#print neue_liste[6]
filename_neu = filename[:filename.find('markers')] + 'chapters.txt'
#print filename_neu
file_neu = open(filename_neu,"w")
file_neu.writelines(neue_liste)
file_neu.close
