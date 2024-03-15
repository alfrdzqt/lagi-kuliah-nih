#%%

def foo(joko):
    agus = 0
    for dini in range(1,joko+1):
        ayu = dini
        agus = agus + ayu
    return agus

print(foo(10))


#%%

def sumOfN(n):
    theSum = 0 
    for i in range(1,n+1):
        theSum = theSum + i 

    return theSum

print(sumOfN(10))

#%%

import time 

def sumOFN2(n):
    start = time.time()

    theSum = 0
    for i in range(1,n+1):
        theSum = theSum + 1

    end = time.time()

    return theSum,end-start

for i in range(5):
    print("hasil disoal 4.2a adalah %d membutuhkanwaktu %10.7f detik" %sumOFN2(10000000))
    print("hasil disoal 4.2a adalah %d membutuhkanwaktu %10.7f detik" %sumOFN2(1000000))
    print("hasil disoal 4.2a adalah %d membutuhkanwaktu %10.7f detik" %sumOFN2(100000))



#%%
    
def sumOFN3(n):
    return (n*(n+1))/2

print("Hasil 10000 iterasi adalah %d"%sumOFN3(10000))
print("Hasil 1000000 iterasi adalah %d"%sumOFN3(1000000))
print("Hasil 100000000 iterasi adalah %d"%sumOFN3(100000000))


#%%

import time

def sumOfY(n):
    start = time.time()
    theSum = 0 
    for i in range(n):
        for j in range(n):
            theSum = theSum + i * j
    end = time.time()
    return theSum, end-start


print("Hasil sumOfY(1000) adalah %d membutuhkan waktu %0.3f detik" %sumOfY(1000))
print("Hasil sumOfY(2000) adalah %d membutuhkan waktu %0.3f detik" %sumOfY(2000))
print("Hasil sumOfY(3000) adalah %d membutuhkan waktu %0.3f detik" %sumOfY(3000))
print("Hasil sumOfY(4000) adalah %d membutuhkan waktu %0.3f detik" %sumOfY(4000))
print("Hasil sumOfY(5000) adalah %d membutuhkan waktu %0.3f detik" %sumOfY(5000))
print("Hasil sumOfY(6000) adalah %d membutuhkan waktu %0.3f detik" %sumOfY(6000))
print("Hasil sumOfY(7000) adalah %d membutuhkan waktu %0.3f detik" %sumOfY(7000))
print("Hasil sumOfY(8000) adalah %d membutuhkan waktu %0.3f detik" %sumOfY(8000))
print("Hasil sumOfY(9000) adalah %d membutuhkan waktu %0.3f detik" %sumOfY(9000))
print("Hasil sumOfY(10000) adalah %d membutuhkan waktu %0.3f detik" %sumOfY(10000))

#%%
import time

def sumOfY(n):
    start = time.time()
    theSum = n * (n+1) * (2*n+1) // 6
    end = time.time()
    return theSum, end-start

print("Hsil sumOfY(1000) adalah %d membutuhkan waktu %0.3f detik" %sumOfY(1000))
print("Hsil sumOfY(2000) adal")

#%%

def anagramSolution1(s1,s2): #mendefinisikan fungsi bernama anagramSolution1 yang menerima dua parameter string, s1 dan s2
    alist = list(s2) # mengubah string s2 menjadi list karakter dan menyimpannya divariabel alist

    pos1 = 0 # menampung index karakter dari string s1 yang sedang di proses
    stillOK = True # variabel boolean yang menandakan apakah s1 masih bisa menjadi anagram dari s2 yang awalnya true

    while pos1 < len(s1) and stillOK: # berjalan selama pos1 belum mencapai akhir s1 dan stillOK masih true
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found: #berjalan selama pos2 belum mencapai akhir alist dan found masih false
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found: # jika found true(karakter ditemukan), set elemen alist[pos2] menjadi none (menandakan karakter tersebut sudah digunakan)
            alist[pos2] = None
        else: # jika found false (karakter ditemukan), set stillOK menjadi false (menandakan s1 tidak bisa menjadi anagram dari s2)
            stillOK = False
        
        pos1 = pos1 + 1

    return stillOK # mengembalikan nilai stillOK

print(anagramSolution1('abcd', 'dcba')) #True (anagram)
print(anagramSolution1('abcd', 'abdc')) #True (anagram) 
print(anagramSolution1('abcd', 'defg')) # False (bukan anagram)

#%%

def anagramSolution2(s1,s2): # mendefinisikan fungsi bernama anagram solution2 yang menerima dua parameter string, s1 dan s2
    alist1 = list(s1) # mengubah s1 dan s2 menjadi list karakter dan menyimpannya di variabel alist1 dan alist2 masing-masing
    alist2 = list(s2) # ini dilakukan karena perbandingan dan pengurutan karakter lebih mudah dilakukan dengan list dibandingkan string

    alist1.sort() # mengurutkan karakter-karakter di alist1 dan alist2 secara alfabetis menggunakan method sort
    alist2.sort() # ini dilakukan karena anagram emiliki susunan karakter yang sama , meskipun urutannya berbeda

    pos = 0 # menampung index karakter yang sedang dibandingkan(awalnya 0)
    matches = True # variabel boolean yang menandakan apakah karakter-karakter dikedua list masih cocok 

    while pos < len(s1) and matches: # perulangan while yang berjalan selama pos belum mencapai akhir s1 dan matches masih true
        if alist1[pos]==alist2[pos]: # jika karakter sama, incremen pos untuk melanjutkan ke karakter berikutnya
            pos = pos + 1
        else: # jika karakter tidak sama, set matches menjadi false (menandakan keduanya bukan anagram)
            matches = False
    
    return matches # mengembalikan nilai matches, fungsi akan mengembalikan true jika semua karakter cocok dan false jika tidak 

print(anagramSolution2('abcde','edcba')) #true (anagram)
print(anagramSolution2('abcde','edcb')) #false (bukan anagram)
print(anagramSolution2('abcde','edfba')) #false (bukan anagram)


#%%

def anagramSolution4(s1,s2): #mendefinisikan fungsi bernama anagram solution 4 yang menerima dua parameter string, s1 dan s2 
    c1 = [0]*26 # meminisiasikan dua list c1 dan c2 dengan panjang 26, masing-masing bernilai 0
    c2 = [0]*26 # list ini akan digunakan untuk menyimpan frekuesi kemuculan setiap huruf alfabet (dari a sampaiz) di kedua string

    for i in range(len(s1)): # i variabel iterasi perulangan
        pos = ord(s1[i])-ord('a') # post variabel untuk menyimpan index posisi karakter di c1 sesuai huruf alfabetnya
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)): # perulangan for yang mirip dengan baris 4-6, namun iterasi sebanyak panjang s2 dan mengisi list c2 dengan frekuensi kemunculan huruf di s2
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0 # memisiasikan j sebagai index iterasi perulangan dan StillOK sebagai flag yang menandakan apakah s1 dan s2 asih berpotensi menjadi anagram (awalnya True)
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False
        
    return stillOK # true jika semua frekuensi kemunculan huruf di kedua string sama (anagram), false jika perbedaan frekuensi kemunculan huruf (bukan anagram)

print(anagramSolution4('apple', 'pleap')) # true
print(anagramSolution4('orange', 'ngerao')) # true
print(anagramSolution4('apple', 'durian')) #false

#%%

