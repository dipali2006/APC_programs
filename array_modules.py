from array import array

# Signed Character
a = array('b', [10, -20, 30])
print("Signed Character:", a)

# Unsigned Character
b = array('B', [10, 20, 30])
print("Unsigned Character:", b)

# Signed Short Integer
c = array('h', [-1000, 2000])
print("Signed Short:", c)

# Unsigned Short Integer
d = array('H', [1000, 2000])
print("Unsigned Short:", d)

# Signed Integer
e = array('i', [-100000, 200000])
print("Signed Integer:", e)

# Unsigned Integer
f = array('I', [100000, 200000])
print("Unsigned Integer:", f)

# Signed Long Integer
g = array('l', [-1234567, 1234567])
print("Signed Long:", g)

# Unsigned Long Integer
h = array('L', [1234567, 7654321])
print("Unsigned Long:", h)

# Signed Long Long Integer
i = array('q', [-1234567890123, 1234567890123])
print("Signed Long Long:", i)

# Unsigned Long Long Integer
j = array('Q', [1234567890123, 9876543210123])
print("Unsigned Long Long:", j)

# Float
k = array('f', [1.5, 2.7, 3.9])
print("Float:", k)

# Double
l = array('d', [1.23456789, 9.87654321])
print("Double:", l)


# Create an integer array
arr = array('i', [10, 20, 30, 40, 20])

print("Original Array:", arr)

# append()
arr.append(50)
print("After append():", arr)

# buffer_info()
print("buffer_info():", arr.buffer_info())

# byteswap()
arr.byteswap()
print("After byteswap():", arr)

# Swap back to original
arr.byteswap()

# count()
print("count(20):", arr.count(20))

# extend()
arr.extend([60, 70])
print("After extend():", arr)

# frombytes()
a = array('i')
a.frombytes(array('i', [1, 2, 3]).tobytes())
print("frombytes():", a)

# fromfile()
f = open("arraydata.bin", "wb")
arr.tofile(f)
f.close()

b = array('i')
f = open("arraydata.bin", "rb")
b.fromfile(f, len(arr))
f.close()
print("fromfile():", b)

# fromlist()
c = array('i')
c.fromlist([100, 200, 300])
print("fromlist():", c)

# fromunicode() (Unicode array)
u = array('u')
u.fromunicode("Hello")
print("fromunicode():", u)

# index()
print("index(30):", arr.index(30))

# insert()
arr.insert(2, 25)
print("After insert():", arr)

# pop()
print("pop():", arr.pop())
print("After pop():", arr)

# remove()
arr.remove(20)
print("After remove(20):", arr)

# reverse()
arr.reverse()
print("After reverse():", arr)

# tobytes()
print("tobytes():", arr.tobytes())

# tofile()
f = open("output.bin", "wb")
arr.tofile(f)
f.close()
print("tofile(): Data written to output.bin")

# tolist()
print("tolist():", arr.tolist())

# tounicode()
print("tounicode():", u.tounicode())
