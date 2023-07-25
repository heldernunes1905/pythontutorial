#function object that remembers values in enclosing scopes even if not in memory
#nested function is a function defined inside another function, nested functions can access variables of enclosed scope, but in python are read only
#print says non bc there is no return so there is nothing to show if ther was a return 3 it would print 3
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    data_transmitter()

print(transmit_to_space("Test message"))

#using nonlocal the variable can change value

def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)


#the reason why this works is bc its being called, the return will function the same as sending the a particular value

def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
fun2()


#since n cannot be changed in this example it remains alwas the same and only one value can be sent at a time so it will stay in the memory until its used
#to return multiplier() it needs to access it and thats where it sees the undefined value and it defines it with the value sent
# if another print is made n remains the same but number will change, cannot add more than one at a time bc return is used only once

def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier


multiplywith5 = multiplier_of(5)
print(multiplywith5(9))


#can do it indefinitely
def multiply_generator(old_function):
    def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator


