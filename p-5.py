#%%

from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append method", t2.timeit(number=1000), "Milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("List comprehension ", t3.timeit(number=1000), "Milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("List Constructor ", t4.timeit(number=1000), "Milliseconds")


#%%

import timeit

popzero = timeit.Timer("x.pop(0)",
                       "from __main__ import x")
popend = timeit.Timer("x.pop()", 
                      "from __main__ import x")


x = list(range(2000000))
popzero.timeit(number=1000)
x = list(range(2000000))
popend.timeit(number=1000)

#%%
import timeit

popzero = timeit.Timer("x.pop(0)",
"from __main__ import popzero, x")
popend = timeit.Timer("x.pop()", "from __main__ import x")

print("pop(0)   pop()")
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.5f, %15.5f" %(pz,pt))


#%%
    
import matplotlib.pyplot as plt
import timeit

def pop_benchmark(x, function_to_time):
    """Times a function's execution with the given list."""
    return function_to_time(x)

data_points = range(1_000_000, 101_000_001, 1_000_000)
pop_zero_times = []
pop_end_times = []

for i in data_points:
    x = list(range(i))
    pop_zero_times.append(timeit.Timer(pop_benchmark, args=(x, x.pop(0))).timeit(number=1000))
    x = list(range(i))  # Recreate the list for accurate timing
    pop_end_times.append(timeit.Timer(pop_benchmark, args=(x, x.pop)).timeit(number=1000))

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(data_points, pop_zero_times, label='pop(0)')
plt.plot(data_points, pop_end_times, label='pop()')
plt.xlabel('List Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Performance Comparison of pop(0) and pop()')
plt.legend()
plt.grid(True)

plt.show()


#%%

import timeit
import random

for i in range(10000,500001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i, "from __main__ import random,x")

    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))


#%%
def kali(a, b):
    for i in range(b):
        b = a + a + a
        return i

print(20 * 3)
kali(20,2)

#%%

def kali(a,b):
    if  a == 1:
        return 1
    else:
        return  a * rekursif(b-1)
    
