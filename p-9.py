#%%
print(15 in [3,5,2,4,1])
print(5 in [3,5,2,4,1])
print(10 in [3,5,2,4,1])

#%%
def sequenstialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found

testList = [1,2,32,8,17,19,42,13,0]
print(sequenstialSearch(testList, 3))
print(sequenstialSearch(testList, 13))

#%%
def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found

testList = [0,1,2,8,13,17,19,32,42]
print(orderedSequentialSearch(testList, 3))
print(orderedSequentialSearch(testList, 13))

#%%

def binarySearch(alist,item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

testList = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testList, 3))
print(binarySearch(testList, 13))

#%%

def binarySearchRecursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearchRecursive(alist[:midpoint], item)
            else:
                return binarySearchRecursive(alist[midpoint+1:], item)

testList = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearchRecursive(testList, 3))
print(binarySearchRecursive(testList, 13))

#%%

print("Nilai ordinal dari karakter c adalah", ord('c'))
print("Nilai ordinal dari karakter a adalah", ord('a'))
print("Nilai ordinal dari karakter r adalah", ord('r'))
print("Nilai ordinal dari karakter i adalah", ord('i'))


#%%
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
    return sum % tablesize

myString = 'cari'
print(hash(myString,11))


#%%

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data #replace
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot] = data #replace

    def hashfunction(self, key, size):
        return key%size
    
    def rehash(self, oldhash, size):
        return (oldhash+1)%size
    
    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

H = HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)

print(H[20])

print(H[17])
H[20]='duck'
print(H[20])
print(H[99])
