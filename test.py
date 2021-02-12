import numpy as np

# 1
print(np.__version__)

# 2
arr = np.arange(10)
print(arr)

# 3
a = np.full((3,3), True, dtype=bool)
b = np.ones((3,3), dtype=bool)
print(a)
print(b)

# 4
arr = np.array([0, 1, 2, 3, 4, 5,  6, 7, 8, 9])
arr = arr[arr % 2 == 1]
print(arr)

# 5
arr = np.array([0, 1, 2, 3, 4, 5,  6, 7, 8, 9])
arr[arr % 2 == 1] = -1
print(arr)

# 6
arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(arr)
print(out)

# 7
arr = np.arange(10)
arr = arr.reshape(2, -1)
print(arr)

# 8
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
one = np.concatenate([a, b], axis=0)
two = np.vstack([a, b])
three = np.r_[a, b]
print(one)
print(two)
print(three)

# 9
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
one = np.concatenate([a, b], axis=1)
two = np.hstack([a, b])
three = np.c_[a, b]
print(one)
print(two)
print(three)

# 10
a = np.array([1,2,3])
ans = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print(ans)