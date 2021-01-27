name = input('What is your name >>> ')

# below is pseudo-code
# ask user to enter his/her yob
yob = input('Which year were you born >>> ')
# calculate his/her age

print(type(yob))
age = 2021 - int(yob)

# print('Hello,', name)
print(f'Hello, {name}!')
print('Your age is', age)
print('After a year, your age will be', age + 1)

