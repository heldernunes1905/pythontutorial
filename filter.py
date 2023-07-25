#filters results so its a true or false thing
#only needs one iterable to work

#example will show every value above 75
# Python 3
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))

print(over_75)



#detects if word is the same backwards and frontwards, only keeps the values that are true and the others are not stored in the list
# Python 3
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)