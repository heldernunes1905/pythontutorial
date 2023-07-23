#instead of doing def sum(a,b): and then return the value there just use a lambda function
#first parameter is the input and second output, so the values being inserted and the operation itself, very useful when doing something small
a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)


#using a function to detect if each element is odd, if it is odd outputs true else outputs false

l = [2,4,7,3,14,19]
for i in l:
    value = lambda i : i % 2 == 1
    print(value(i))