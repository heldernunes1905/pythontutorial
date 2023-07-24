#simple way to create a data structure using json
import json
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)

#python has their own method of creating a data structure
import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))



import json

#get the salaries in json format, then decode it into a format python can read, add the data to the list and then send the value in json format


# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    # Add your code here
    salaries = json.loads(salaries_json)
    salaries[name] = salary #to add we use the id and then the value give, for example, if the value of object name was Le it would then show Le as the name, this just add data into the list nothing else.

    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])