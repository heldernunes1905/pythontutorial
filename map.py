#make pet names uppercase normally
my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []

for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)

print(uppered_pets)

#pet names uppercase using a map
#maps need an iterable so my_pets will do
# Python 3
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)



# Python 3
#in this case the iterable will go through each of them and each one it will count more so this is the same as round(3.56773, 1) and second one is round(5.57668, 2), it will keep going until the list is done
#both are iterable and when one misses/ends it will stop at it
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1, 7)))

print(result)


# Python 3
#uses 2 lists and creates just one using both of the elements, it stops when one of them reaches the end
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(zip(my_strings, my_numbers))

print(results)#[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]



# Python 3

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)


# Python 3
#creates the same result, i can see it being useful like if I need to multiply like the same index of 2 different lists
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)
