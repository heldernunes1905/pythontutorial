astring = "Hello world!"
print("single quotes are ' '")

print(len(astring)) #length of string

astring = "Hello world!"
print(astring.index("o")) #index of first o

astring = "Hello world!"
print(astring.count("l")) #count number of letter l in string

astring = "Hello world!"
print(astring[3:7]) #get from index 3 to 6

astring = "Hello world!"
print(astring[3:7:2]) #index 3 to 6 and skips one character

astring = "Hello world!"
print(astring[::-1]) #invert string

astring = "Hello world!"
print(astring.upper()) #all upppercase
print(astring.lower()) #all lowercase


astring = "Hello world!"

#will check if string starts with that string of characters or it ends with them
print(astring.startswith("Hello")) #true
print(astring.endswith("asdfasdfasdf")) #false


astring = "Hello world!"
afewwords = astring.split(" ") #will split at a space and add it to a list so the list will be 2 index long and each index with have a word, if the split had l it would split whenever it saw that character


s = "Strings are awesome"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))