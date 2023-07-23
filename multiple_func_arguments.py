#dinamic function which is very useful, the first 3 arguments are mandatory and function will not work without them, the last one is not, function will work if its empyy
# if there are 6 variables, the first 3 go to the first 3 objects and the rest to the one with the * on it

def foo(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

foo(1, 2, 3, 4, 5, 6)


#can send function arguments
#the argument action has a value of sum and if its sum it will print out the sum
#argument number has a value of first and it will return value of first which is 1, since its a function object result gets a value of 1

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))


#foo checks amount of extra arguments sent and then print something based on the result
#bar will check the number sent, if its 6 doesnt do anything meaning its false but if its 7 it exists there meaning its true.

# edit the functions prototype and implementation
def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwars):
    return kwars["magicnumber"]==7


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")