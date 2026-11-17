import math

def luas_kubus(s):
    hasil = 6 * s ** 2
    print("luas permukaan kubus sisi =", s, "adalah", hasil)

def luas_tabung(r, t):
    hasil = 2 * math.pi * r * (r + t)
    print("luas permukaan tabung r =", r, "t =", t, "adalah", hasil)

def luas_bola(r):
    hasil = 4 * math.pi * r ** 2
    print("luas permukaan bola r =", r, "adalah", hasil)