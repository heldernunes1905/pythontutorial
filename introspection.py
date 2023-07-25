# Use the help function to see what each function does.
# Delete this when you are done.
help(dir)#names in current scope so objects, no value just the object names
help(hasattr)#return if object has attribute with given name, hasattr(name) will return true but hasattr(id) will return false
help(id)# return identity of an object, its always random

# Define the Vehicle class.
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Print a list of all attributes of the Vehicle class.
# Your code goes here
print(dir(Vehicle()))