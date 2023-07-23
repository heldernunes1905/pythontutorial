import random

#yield basically is like a quick save point, it doesnt save anything in memory
#all its capable of doing is restoring a certain point, for example when its done with current iteration yield will be able to restore that comand
#function is paused when done and can be resumed again after the command is called, this way several values can be sent individually instead of being sent as a list.

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)
    yield random.randint(20, 35)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))#



#finobacci series
#create 2 variables with a value of 1 each
#the next value is the sum of the previous 2 values so 1+0=1,1+1=2,2+1=3,3+2=5
#2 values of 1 and 1, value of a becomes the value of the previous sum and b becomes the value of the new sum

# fill in this function
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a+b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break