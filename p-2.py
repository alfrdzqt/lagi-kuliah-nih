#%%

a = 12
b = 42



print(a+b*4) # Output: 180 Integer
print((a+b)*4) # Output: 216 Integer
print(a**10) # Output: 61917364224 Float
print(a/3) # Output: 4.0 Float
print(b/3) # Output: 14.0 Float
print(a//b) # Output: 0 Integer
print(a&b) # Output: 8 Integer
print(a/b) # Output: 0.2857142857142857 Float
print(a//b) # Output: 0 Integer
print(a&b) # Output: 8 Integer
print(b**100) # Output: 2113143741011360736530044045523113991698878330713580061264477934391564919875497777688215057732151811172029315247932158994879668553186145824710950394684126712037376 Integer

#%%
a = 12
b = 42

print(a == b)
print(b > a)
print(b >= 1) and (b <= 10)
print(a != b)
print(a and b)
print(a or b)
print(not a)
print(not b)

# Output:
# False
# True
# True
# True
# 42
# 12
# False
# False

#%%
myNim = str(2311102441242)

myNim_10th = myNim[9]
myNim_11th = myNim[-3]
i = 11
myNim_12th = myNim[1]
myNim_13th = myNim[i+1]
a = int(myNim_10th + myNim_11th)
b = float(myNim_12th + myNim_13th)
print(myNim)
print(myNim_10th)
print(myNim_11th)
print(myNim_12th)
print(myNim_13th)
print(a)
print('nilai float b = ',b)

# Output:
# 2311102441242
# 1
# 2
# 3
# 2
# 12
# nilai float b =  32.0

#%%
myList = [1,3,True,6.5]
print(myList)
A = [myList]*3
print(A)
myList[2] = 45
print(A)

myList_A = [1024, 3, True, 6.5]
myList_A.append(False)
print(myList_A)
myList_A.insert(2,4.5)
print(myList_A)
print(myList_A.pop())
print(myList_A)
print(myList_A.pop(1))
print(myList_A)
myList_A.pop(2)
print(myList_A)
myList_A.sort()
print(myList_A)
myList_A.reverse()
print(myList_A)
print(myList_A.count(6.5))
print(myList_A.index(6.5))
myList_A.remove(6.5)
print(myList_A)
del myList_A[0]
print(myList_A)

newList = myList + myList_A
print(newList)
print(len(myList))
print(myList[:2])

# [1, 3, True, 6.5]
# [[1, 3, True, 6.5], [1, 3, True, 6.5], [1, 3, True, 6.5]]
# [[1, 3, 45, 6.5], [1, 3, 45, 6.5], [1, 3, 45, 6.5]]
# [1024, 3, True, 6.5, False]
# [1024, 3, 4.5, True, 6.5, False]
# False
# [1024, 3, 4.5, True, 6.5]
# 3
# [1024, 4.5, True, 6.5]
# [1024, 4.5, 6.5]
# [4.5, 6.5, 1024]
# [1024, 6.5, 4.5]
# 1
# 1
# [1024, 4.5]
# [4.5]
# [1, 3, 45, 6.5, 4.5]
# 4
# [1, 3]


#%%
myTuple = (2,True,4.96)
print(myTuple)
print(len(myTuple))
print(myTuple[0])
print(myTuple * 3)
print(myTuple[0:2])
myTuple[1] = False

#Output:
# (2, True, 4.96)
# 3
# 2
# (2, True, 4.96, 2, True, 4.96, 2, True, 4.96)
# (2, True)

#%%
myTuple = (2,True,4.96)
print(myTuple)
print(len(myTuple))
print(myTuple[0])
print(myTuple * 3)
print(myTuple[0:2])
myTuple[1] = False

#Output:
# (2, True, 4.96)
# 3
# 2
# (2, True, 4.96, 2, True, 4.96, 2, True, 4.96)
# (2, True)

#%%

capitals = {'KalTim' : 'Samarinda', 'Bali' : 'Denpasar'}
print(capitals['KalTim'])
capitals['JaTim'] = 'Surabaya'
print(capitals)
capitals['KalSel'] = 'Banjarmasin'
print(len(capitals))
for k in capitals:
    print(capitals[k],"adalah ibukota dari ",k)

product = {
    'name': 'Pisang',
    'price': 5.800,
    'stock': 10
}
print(product)

#Output: 
# Samarinda
# {'KalTim': 'Samarinda', 'Bali': 'Denpasar', 'JaTim': 'Surabaya'}
# 4
# Samarinda adalah ibukota dari  KalTim
# Denpasar adalah ibukota dari  Bali
# Surabaya adalah ibukota dari  JaTim
# Banjarmasin adalah ibukota dari  KalSel
# {'name': 'Pisang', 'price': 5.8, 'stock': 10}

#%%

aName = input("Nama lengkap saya adalah ")
print("Huruf kapital untuk nama anda ",aName.upper(),"dan mempunyai karakter sebanyak ",len(aName))

#Output: 
# Huruf kapital untuk nama anda  SYERA AL-FARIDZ dan mempunyai karakter sebanyak  15


#%%

sisiKubus = input("Input nilai sisi persegi")
sisi = float(sisiKubus)
luas = 2 * sisi
print('Luas persegi yaitu ',luas)

#Output: 
# Luas persegi yaitu  8.0


#%%

aName = input('Nama: ')
myNim = input('NIM: ')

print(aName,myNim)
print(aName,myNim, sep='-',end='.')
print("%s mempunyai NIM %i" % (aName,myNim))

#Output:
# SYERA AL-FARIDZI 2311102441242
# SYERA AL-FARIDZI-2311102441242.

#%%

price = 5800
item = 'pisang'
print("Harga sebuah %s adalah %d rupiah"%(item,price))
print("Harga sebuah %+10s adalah %5.2f rupiah"%(item,price))
print("Harga sebuah %+10s adalah %10.2f rupiah"%(item,price))
itemdict = {"item" : "pisang", "harga" : 6800}
print("Harga sebuah %(item)s adalah %(harga)7.1f rupiah"%itemdict)

#Output:
# Harga sebuah pisang adalah 5800 rupiah
# Harga sebuah     pisang adalah 5800.00 rupiah
# Harga sebuah     pisang adalah    5800.00 rupiah


#%%

n = 100

if n < 0 :
    print("Sorry, value is negative")
else:
    print(Math.sqrt(n))