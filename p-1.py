#%%
# %%python3
x = 12
y = 42

Ha = x + y
print(Ha)
# output: 54

Hb = Ha + 10.5
print(Hb)
# output: 64.5

Hc = int(Hb)
print(Hc)
# output: 64

Hd = Ha / Hb
print(Hd)
# Output: 0.8372093023255814

print(isinstance(Hd, int))
print(isinstance(Hd, float))
if isinstance(Hd, int):
    print('Hd adalah integer!')
else:
    print('Hd adalah bilangan float!')
# Output: Hd adalah bilangan float!



#%%

(999).bit_length()
# Output 10

#%%
(998).bit_length()
# Output 10

#%%
(99).bit_length()
# Output 7

#%%
(11).bit_length()
# Output 4

#%%
i = 555

print(bin(i))
# Output 0b1011111011
print(hex(i))
# Output 0x22b
print(oct(i))
# Output 0O1053

