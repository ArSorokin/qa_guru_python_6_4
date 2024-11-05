import random

myDict = {}

first = ["a", "b", "c", "d", "e"]
second = [1, 2, 3, 4, 5]

n = 10
# [random.randint(0, 100) for i in range(n)]

myDict[1] = first
myDict["key2"] = ["Geeks", "For", "Geeks"]

# Adding list as value
myDict["key1"] = [1, 2]
# myDict["key2"] = ["Geeks", "For", "Geeks"]

print(myDict)
print(list(myDict.items()))

myDict["key2"].append("2")

print(myDict)

l = []
amount = len(l)

while len(l) < 10:
    l.append(random.randint(1, 100))
    # l.append(random)
    amount = len(l)
    print(amount)

print(l)

a = "123"
print(a)
print(type(a))
b = int(a)
print(b)
print(type(b))


# Создание словарей

first = ["one", "two", "three", "four", "five"]
second = [1, 2, 3, 4, 5]
dict1 = dict(zip(first, second))

print(dict1)

# assert len(l) == 10
# assert l[0] < l[-1]


# a = 0.1 + 0.2
# print(round(a, 18))
# print(a)
# a = 1.228
# print(round(a, 2))
# print(a)