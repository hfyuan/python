import numpy as np

array1 = np.array(range(6,21,2))
print(array1)

array2 = array1.reshape(2,4)

print("array1:")
print(array1)

print("array2:")
print(array2)

array1[0] = 999

print("array1:")
print(array1)

print("array2:")
print(array2)

array3 = np.linspace(1,12,12,dtype=int)
array4 = np.linspace(1,12,6)

print(array3)
print(array4)

array5 = np.zeros((3,3))
print(array5)
array6 = np.ones((2,3,4,5),dtype=np.int64)
print(array6)

na1 = np.array(np.arange(24),dtype=int).reshape(4,6)

print(na1)

print(na1[:2,1:])

print(na1[2:,[2,3]])

na2 = na1.reshape(2,3,4)

print(na2)

print(na2[[1,1,0],[0,1,2],[2,3,1]])


nr1 = np.array(np.arange(5))
print(nr1)

print(np.add(nr1,4))
nr2 = np.array([2,3,4,5,6])
print(nr2)

nr3 = nr1+nr2
print(nr3)

nr4 = np.add(nr1,nr2)
print(nr4)

np.add(nr1,nr2, nr1)
print(nr1)



A= np.arange(1, 11)
print(A)

B= np.arange(0, 10)[:, np.newaxis]
print(B)

C = (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
print(C)

X = 1. / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
print(X)

print("---------------------------------------------")
myar = np.zeros((10,10))
for arI in np.arange(1,11):
    for arJ in np.arange(1,11):
        myar[arI-1,arJ-1] = 1./(arI+arJ-1)
        print(myar[arI-1,arJ-1])
print(myar)


print("11111111111111111111111111111111111111111111")

mylist = [0.5,1.43,-1.36,-0.16,0.29,-0.59,1.16,-0.33,0.07,-1.36]

myarray = np.array(mylist)
print("the array is :")
print(myarray)

print(" the np.mean :" )
print(np.mean(myarray))

print("the median is :")
print(np.median(myarray))

print("the var is :")
print(np.var(myarray))

print("the std is :")
print(np.std(myarray))

