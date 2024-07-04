"""
index = 0
while index <= 100:
    index += 1
    if index %2 == 0:
        continue
    print(index)

sum = 0
usnumber = int(input("Enter number\t"))
for elem in range(0, 10):
    sum = usnumber * elem
    print(sum)


sum = 0
for i in range(1, 50):
    if i %2 == 0:
        sum += i
        print(sum)

for i in range(11):

    for j in range(11):
        if i + j == 10:
            print("*  ", end="")
        else:
            print(" ", end=" ")
    print()


import random

randNumber = random.randint(0,100)

step = 0

while True:
    userInput=int(input("Enter your number from 0 to 100: \t"))
    step+=1
    if userInput == randNumber :
        print(f"YOU WIN, your try {step}")
        break
    elif userInput < randNumber:
        print("Rand number more than your")
    elif userInput > randNumber :
        print("Rand number less than your")
    elif userInput <0 or userInput > 100:
        print("Try another number")


import random

sum = 0
for number in range(0, 16):
    number = random.randint(0, 100)
    print(number)
    if sum < number:
        sum = number
print(number)



import random

for num in range(0, 9):
    nums = random.randint(0,9)
    print(nums, end = " ")


import random
sum = 0
sum1 = 0
for a in range(0, 101):
    nums = random.randint(0,1)
    if nums == 0:
        sum += 1
    elif nums > 0:
        sum1 += 1
if sum > sum1:
    print("Reshka")
else:
    print("Orel")


a = int(input('Введите число а: '))
b = int(input('Введите число b: '))

numbers = [x for x in range(a, b + 1)]

average = (sum(numbers)/float((len(numbers))))
print('Среднее арифметическое этих чисел: ', average)

sum = 0
for z in range(0, 1001):
    a = 0
    b = 1000
    sum = ((a + 1) + (b - 1)) / 2
    print(sum)



sum = 0
while True:
    a = int(input("Enter number\t"))
    if a > 0 and a <= 20:
        sum += a
        print(sum)
    else:
        print("Error")

    print(username.lower()) # переворить рядок у нижній регістр
    print(username.upper())# переворить рядок у верхній регістр
    print(username.lstrip()) # забрає пробіл ліворуч
    print(username.rstrip()) # забрає пробіл праворуч
    print(username.strip()) #забрає пробіл праворуч та ліворуч
    print(username.strip().lower())

import random
import string

user = int(input("Enter num\t"))

pin = ""

strok = string.ascii_letters + string.digits + string.punctuation

for index in range(user):
    pin += random.choice(strok)
print(pin)

my_list = ["name1", "name2", "name3", "Andrey", 25, 67]


for index in range(len(my_list)):
    print(f"Elem: {my_list[index]}, Index: {index} ")

"""