#split is dividing the current sentence into parts and making a list of it, each word becomes an item in the list
#for loop goes throught every bit of the list and the if statement states that if the word is not "the" the list word_lengths has values added to it
#in this case its the length of the word but it could be the word itself 
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)

#list comprehension makes it easier to simplify the process
# we can say it all in a sentence, get length of word in each element of the list where the element doesnt have a value of "the"
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)


#runs through the array and if a number is positive it gets added to this list after it gets turned into an int
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(number) for number in numbers if number > 0]
print(newlist)