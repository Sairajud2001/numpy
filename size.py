import numpy 
import time
import sys

##---------------------------size
a=range(1000)
print(len(a))
print(sys.getsizeof(105)*len(a))
# `print(sys.getsizeof(105)*len(a))` is calculating the total memory size occupied by the list `a` in
# bytes.
array=numpy.arange(1000)

# `print(array.size*array.itemsize)` is calculating the total memory size in bytes occupied by the
# numpy array `array`.
print(array.size*array.itemsize)


#------------time
size=10000000
a1=numpy.arange(size)
a2=numpy.arange(size)
start=time.time()
#list adding
result1=[(x+y) for x,y in zip(a1,a2)]
print("time taken for the list",(time.time()-start)*1000)
# using numpy
start=time.time()
result2=a1+a2
print("time taken for the numpy",(time.time()-start)*1000)

#output
#time taken for the list 1377.2141933441162
#time taken for the numpy 18.048524856567383