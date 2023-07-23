#sets are lists without duplicate entries
print(set("my name is Eric and Eric is my name".split()))

#this will check for same values in both lists so john
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print(b.intersection(a))


#this checks for values in only one, can create a list with both
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))


#this checks for values in only one, different lists
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.difference(b))
print(b.difference(a))


#one list and will get all the names but no duplicates
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.union(b))


#will turn the lists into sets, difference will make only one list using list A and will remove every duplicate that exists in list b
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

A = set(a)
B = set(b)

print(A.difference(B))