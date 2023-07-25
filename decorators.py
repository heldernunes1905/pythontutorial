#basically change name of functions and other stuff
def type_check(correct_type):#correct_type is the actual type, like the one being sent
    def check(old_function):#old function is the first function so times2 and first_letter
        def new_function(arg):#arg is the value being sent so all the values need to pass through here before reaching the intended function
            if (isinstance(arg, correct_type)):#checks if value sent is the same of the type originally sent
                return old_function(arg)#since old_function is defined below it will send the value and arg is the first one so its 2, it only does the math below
            else:
                print("Bad Type")
        return new_function
    return check


#generator
#its reassigning the old name into the new one
@type_check(int)#value being sent is an int
def times2(num):#it needs to wait for everything to be done before it can actually do anything and is only done is the function above calls it
    return num*2#send this value to type_check

print(times2(2))
times2('Not A Number')#since it was reassigned that the function should take int it would trigger the else statement in the if



@type_check(str)#reassign the function do a string
def first_letter(word):#it needs to wait for everything to be done before it can actually do anything and is only done is the function above calls it
    return word[0]#send this value to type_check

print(first_letter('Hello World'))#sends a string to first_letter
first_letter(['Not', 'A', 'String'])#send the whole list and then it will send the first element to check if its the same thing