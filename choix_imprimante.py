#!/usr/bin/env python3

import os

def printer():
    cmd = "lpstat -a | cut -f1 -d' '"
    sortie=(os.popen(cmd).read()).split()
    rep=False
    for i in sortie:
        rep = input(i+' : Voulez-vous utiliser cette imprimante ? (O/N) : ')
        if rep=="o":
            imp=i
            print('Imprimante choisie : \n'+imp)
            return imp
        else:
            rep="n"
        #if
    #for
    print("Aucune imprimante %s" % ("choisie" if rep else "installée"))
# printer

if __name__ == "__main__":
    printer()
# if
