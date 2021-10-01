# Python program to demonstrate working
# of map.

# Return double of n
# def addition(n):
# 	return n + n

# We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))


# Double all numbers using map and lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))
print(result)
print(type(result))
