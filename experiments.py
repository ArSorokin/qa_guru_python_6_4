import random

myDict = {}

first = ["a", "b", "c", "d", "e"]
second = [1, 2, 3, 4, 5]

n = 10
# [random.randint(0, 100) for i in range(n)]

myDict[1] = first
myDict["key2"] = ["Geeks", "For", "Geeks"]

# Adding list as value
# myDict["key1"] = [1, 2]
# myDict["key2"] = ["Geeks", "For", "Geeks"]

print(myDict)
print(list(myDict.items()))

a = 0.1 + 0.2
print(round(a, 18))
print(a)
a = 1.228
print(round(a, 2))
print(a)