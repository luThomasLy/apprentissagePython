import numpy

v1 = numpy.array([1,2,3])
v2 = numpy.array([1,2,3,4])
m = min(len(v1),len(v2))
print(v1[:m]/v2[:m])