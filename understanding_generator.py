# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)

# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(x.__next__()) # In Python 3, __next__()
print(x.__next__())
print(x.__next__())


# Usage - For converting whole block into chunks and then process chunks one by one
# example - Let's assume we have 5 lakhs of entries in DB, so we will convert it to generator() as 50k chunks, so process 1st chunk and then process next