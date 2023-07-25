#basically cut the function into 2 different calls, the second number being called will be the last one so in the example 2 x = 1
#if i put print(dbl(4)) below it will do the math but do 4 instead of 1, which is very useful if certain values need to static and one dynamic


from functools import partial

def multiply(x, y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply, 2)
print(dbl(4))


#Following is the exercise, function provided:
from functools import partial
def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function 
dbl = partial(func,10,5,2)
print(dbl(1))