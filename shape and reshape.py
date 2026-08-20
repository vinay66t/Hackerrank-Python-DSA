import numpy
arr = input().strip().split()
arr = numpy.array(arr,int)
matrix = arr.reshape(3,3)
print(matrix)
