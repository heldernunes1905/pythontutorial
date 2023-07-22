number = 1 + 2 * 3 / 4.0 #2.5

remainder = 11 % 3 # gets remainder of operation which is 2

squared = 7**2 #does square of 7 so 7*7
cube = 2**3 #does cube of 2 so 2*2*2

manyhello = "hello" * 10 #this will do the word hello 10 times

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]

all_numbers = odd_numbers + even_numbers # will combine the 2 lists together, odd comes first and then even

lotoflists = [1,2,3] * 3 #will make a list using the values in that one but makes it 3 times so its 1,2,3,1,2,3,1,2,3


#list with no values and then changed to have 10 values
#after that big_list is the joint connection of the 2 other lists

x = object()
y = object()

# TODO: change this code
x_list = [x]*10
y_list = [y]*10
big_list = x_list+ y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")