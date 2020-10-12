#! /usr/bin/env python3
import sys
import re

for line in sys.stdin:
    # Ajout  ,.:;?")""("0123456789
    # Supprimer les espaces
    line = line.strip()
    # recupérer les mots
    words = line.split()

    # operation map, pour chaque mot, generer la paire (mot, 1)
    for word in words:
        k = word.strip('\*- ,.:;?)(\"0123456789')
        if len(k) != 0:
            print("%s\t%d" % (k, 1))
