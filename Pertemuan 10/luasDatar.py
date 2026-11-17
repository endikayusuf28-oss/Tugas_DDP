import math

def luas_lingkaran(r):
    hasil = math.pi * r ** 2
    print("luas lingkaran r =", r, "adalah", hasil)

def luas_persegi(s):
    hasil = s * s
    print("luas persegi sisi =", s, "adalah", hasil)

def luas_segitiga(alas, tinggi):
    hasil = 0.5 * alas * tinggi
    print("luas segitiga alas", alas, "tinggi", tinggi, "adalah", hasil)