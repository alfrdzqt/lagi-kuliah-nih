#%%

counter = 1
while counter <= 5:
    print("Hallo, Nim saya: 2311102441242")
    counter = counter + 1

counter = 1
while counter <= 10:
    print("Hallo, Nim saya: 2311102441242")
    counter = counter + 1

# Output
# Hallo, Nim saya: 2311102441242
# Hallo, Nim saya: 2311102441242
# Hallo, Nim saya: 2311102441242
# Hallo, Nim saya: 2311102441242
# Hallo, Nim saya: 2311102441242

# Output
# Hallo, Nim saya: 2311102441242
# Hallo, Nim saya: 2311102441242
# Hallo, Nim saya: 2311102441242
# Hallo, Nim saya: 2311102441242
# Hallo, Nim saya: 2311102441242
# Hallo, Nim saya: 2311102441242
# Hallo, Nim saya: 2311102441242
# Hallo, Nim saya: 2311102441242
# Hallo, Nim saya: 2311102441242
# Hallo, Nim saya: 2311102441242


#%%
    counter = 0
while counter < 10:
    print(counter, "Kurang dari 10")
    counter = counter + 1
else: 
    print(counter, 'sama dengan 10')


#%%

daftarkata = ['saya', 'anda', 'dia']
daftarhuruf = [ ]
for setiapkata in daftarkata:
    for setiaphuruf in setiapkata:
        daftarhuruf.append(setiaphuruf)
print(daftarhuruf)

# Output:
# ['s', 'a', 'y', 'a', 'a', 'n', 'd', 'a', 'd', 'i', 'a']

#%%

import math
n = -2

if n < 0:
    print("maaf, nilai yang di input adalah negatif")
else:
    print(math.sqrt
    (n))

# Output n = 2
# 1.4142135623730951

# output n = -2
# maaf, nilai yang di input adalah negatif


#%%

SQlist = []
for x in range(1,11):
    SQlist.append(x*x)
print(SQlist)

STlist = [x*x for x in range(1,11)]
print(STlist)

# Output:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#%%

score = int(input("Masukkan skor: "))

if score >=90:
    print("A")
else:
    if score >=80:
        print("B")
    else:
        if score >=70:
            print("C")
        else:
            if score >=60:
                print("D")
            else:
                print("E")

#%%
                
namatanpakosonan = [ch.upper() for ch in 'syera al-faridzi' if ch not in 'AEIOU']
print(namatanpakosonan)

# Output:
# ['S', 'Y', 'E', 'R', 'A', ' ', 'A', 'L', '-', 'F', 'A', 'R', 'I', 'D', 'Z', 'I']

#%%

import math

try:
    anumber = int(input("Masukan nilai integer "))
    print(math.sqrt(anumber))
except ValueError:
    print("Nilai harus integer")
finally:
    print('Program selesai')

# Output:
# Nilai harus integer
# Program selesai
    

#%%

def kuadrat(x):
    return x * x
kuadrat(2)

# Output:
# 4


#%%

def luasLingkaran(r):
    return 3.14 * r * r

luasLingkaran(7)

# Output:
# 153.86

#%%

def luasSegitiga(a, t):
    return 0.5 * a * t

luasSegitiga(10, 5)

# Output:
# 25.0

#%%

class Fraksi:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = self.gcd(newnum, newden)
        return Fraksi(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def gcd(self, m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n 

# Contoh penggunaan
f1 = Fraksi(1, 4)
f2 = Fraksi(1, 2)

print(f1 + f2)

x = Fraksi(1, 2)
y = Fraksi(2, 3)
print(x + y)
print(x == y)

# Output:
# 3/4
# 7/6
# False

#%%

class Fraksi:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

myFraksi = Fraksi(3,5)
print(myFraksi)

# Output:
# <__main__.Fraksi object at 0x000001F7879A9C90>