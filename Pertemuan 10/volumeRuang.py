import math

def volume_kubus(s):
    hasil = s ** 3
    print("volume kubus sisi =", s, "adalah", hasil)

def volume_tabung(r, t):
    hasil = math.pi * r ** 2 * t
    print("volume tabung r =", r, "t =", t, "adalah", hasil)

def volume_bola(r):
    hasil = 4 / 3 * math.pi * r ** 3
    print("volume bola r =", r, "adalah", hasil)