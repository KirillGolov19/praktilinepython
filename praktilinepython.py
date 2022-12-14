from math import *
from random import *
try:
    a=int(input("Sisestage number: "))
    if(a>0):
        print("Positiivne arv")
    else:
        print("Negatiivne arv")
    if a%2==0:
        print(f"{a} on paaris")
    else:
        print(f"{a} on paaritu")
except:
    print("Vale andmetüüp")

#
