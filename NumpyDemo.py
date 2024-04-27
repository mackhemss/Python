import numpy as np

data = np.random.rand(2,3,4)
zeros = np.zeros((2,2,2))
full = np.full((2,2,2),7)
once = np.ones((2,2,2))

# Attributes
shape = data.shape
size = data.size
types = data.dtype

# Slicing
arr = data[0]
slicer = data[0][0:2]
reverse = data[-1]
singleval = data[0][0][0]

list1 = np.random.rand(10) 
list2 = np.random.rand(10) 

# Basic Math
add = np.add(list1, list2)
sub = np.subtract(list1, list2)
div = np.divide(list1, list2)
mult = np.multiply(list1, list2)
dot = np.dot(list1, list2)

# Stat Functions
sqrt = np.sqrt(25)
ab = np.abs(-2)
power = np.power(2,7)
log = np.log(25)
exp = np.exp([2,3])
mins = np.min(list1)
maxs = np.max(list1)

data.sort()

data = data.reshape((2,2,-1))

zeroes = np.zeros((8))
print(zeroes)
zeroes = np.append(zeroes, [3,4])
print(zeroes)

zeroes = np.insert(zeroes, 2, 1)
print(zeroes)

np.delete(data, 0, axis=1)

np.save("new array", data)

test = np.load("new array.npy")

print(once)