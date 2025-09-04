import numpy

a = numpy.zeros((20, 20, 20, 20, 20, 20, 20))

def Constructo(index_max: int, size: int, index_current: int = 0):
    if index_current >= index_max - 1:
        return [i for i in range(size)]
    else:
        return [Constructo(index_max, size, index_current + 1) for _ in range(size)]

for i in range(1, 3):
    print(f"Size of: {i}")
    print(numpy.array(Constructo(i, 5)))
    print("-" * 25)