"""
Это примеры работы со строками
"""
# Учимся писать строки!

s = "Hello, world!"
print(s + "1")
s = "Hello, \" world!"
print(s + "2")
s = 'Hello, world!'

s = """Hello, world!"""
s = '''Hello, world!'''

print(s + "3")

s = """Hello, 
world!"""

print(s + "4")

s = "Hello, \n" \
    "world!"

print(s + "5")

s = "Hello, \nworld!"

print(s + "1")

# Сырые строки

raw_string = r"\n\r\fasofpjupwof''23\r12\r1\2\124\v\v34" r"'\n\r\fasofpjupwof''23\r12\r1\2\124\v\v34'"

print(raw_string)

# Индексы и слайсы

email = "user@domain.com"

s = "abcdef"

print(s[0])
print(s[0:3])
print(s[::-1])
print(s[4::-2])

# Оперируем

s = "abc".upper()
print(s)

# Форматируем

a = "Hello"
b = "World"

print(a + ", " + b + "!")

print(f"{a}, {b.upper()}!")

print("{}, {}!".format(a, b.upper()))

print("{first}, {second}!".format(first=a, second=b.upper()))

url_template = "https://yourservice.com/v1/api/{}"
get_users_url = url_template.format("users")
get_groups_url = url_template.format("groups")
print(get_groups_url)
print(get_users_url)

# Строку в число, и наоборот

s = "1234"
n = 1234


# assert s == n
assert int(s) == n
assert s == str(n)

a = 'abc'
aa = a
