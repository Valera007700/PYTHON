# number = 1
# while number <= 10:
#     number = int(input("What is the number? "))
#
# print("finished with the loop")


# import time
# number_1 = -100
# while number_1 <= 5:
#     print(f"The number is: {number_1}")
#     number_1 = number_1 + 1
#     time.sleep(0.1)
# print("finished with the loop")


# for name in ['Valery', 'Ivanka']:
#     print(name)

# edibles = ["отбивные", "пельмени", "яйца", "орехи"]
# # for food in edibles:
# #     if food == "пельмени":
# #         print("I don't like пельмени!!!")
# #         continue
# #     print("I really like " + food)
# # else:
# #     print("I hate пельмени!!!!!!!")
# # print("We have finished")

# i = 1
# for color in ["red", "blue", "orange", "green", "black"]:
#     print("#", i, "color of rainbow is", color)
#     i += 1


# tools = ['hammer', 'bug', 'car']
# for m in tools:
#     print(f"The item is: {m}")


# numbers = range(10)
# for number in range(10):
#     number += 1  # добавил 1 цифру к массиву, потому что по стандарту идёт 0 = 1
#     print(number)


# for i in range(100, 200, 10):
#     print(i)

#todo _________________

# from ctypes.wintypes import FLOAT
#
#
# childs_meal = input ("What is the price of a child's meal?  ")
# adults_meal = input ("What is the price of an adult's meal?  ")
#
# many_children = input ("How many children are there?  ")
# many_adults = input ("How many adults are there?  ")
#
# tax_rate = input ("What is the sales tax rate?")
# childs = (float(childs_meal)) * (float(many_children))
# adults = (float(adults_meal)) * (float(many_adults))
# subtotal = (float(childs)) + (float(adults))
# sales_tax = ((float(subtotal)) * (int(tax_rate)) / 100)
# total = sales_tax + subtotal
#
#
#
#
#
# print ("Subtotal: ", subtotal)
# print ("Sales Tax: ", sales_tax)
# print ("Total: ", total)
#
# payment  = input ("What is the payment amount?  ");
# change = ((int(payment)) - total)
# change_2 = round(change, 2)
# print("Change: " ,change_2)
#
#
# #print (int(firts_num) + int(second_num))
#
#
# #todo _______________________________________
#
# from ctypes.wintypes import FLOAT
# import math
#
# cars = 3;
# people = 8;
# people_per_car = people/cars
# print(f"There are {people_per_car:.2f} people in each car")
# print(f"There are {people_per_car:.1f} people in each car")
# print(f"There are {people_per_car:.3f} people in each car")
#
# first = int (input("number of my ice-cream: "))
# second = int (input("how many? "))
# result = first/second
# print(f"how_many_for_instance {result:0f} in my hand")
# print("###############################################")
#
#
#
# big_number = 13346817564269542565
# print(f"The number is: {big_number:,} hereeeee")
# print("###############################################")
#
# radius = 5
# area = math.pi * (radius ** 2)
# print(f"The area is: {area:3f}")
# print("###############################################")
#
#
#
# weight = 1.62
# lower = math.floor(weight)
# print(lower)
#
# lower = math.ceil(weight)
# print(lower)
# print("###############################################")
#
#
#
#
#
# childs_meal = input ("What is the price of a child's meal?  ");
# adults_meal = input ("What is the price of an adult's meal?  ");
#
# many_children = input ("How many children are there?  ");
# many_adults = input ("How many adults are there?  ");
#
# tax_rate = input ("What is the sales tax rate?")
# childs = (float(childs_meal)) * (float(many_children))
# adults = (float(adults_meal)) * (float(many_adults))
# subtotal = (float(childs)) + (float(adults));
# sales_tax = ((float(subtotal)) * (int(tax_rate)) / 100)
# total = sales_tax + subtotal
#
#
# print ("Subtotal: ", subtotal)
# print ("Sales Tax: ", sales_tax)
# print ("Total: ", total)
#
# payment  = input ("What is the payment amount?  ");
# change = ((int(payment)) - total)
# change_2 = round(change, 2)
# print("Change: " ,change_2)
# print("###############################################")
#
#
# amount = (int(input ("What is your favorite number? ")))
#
# if amount == "123":
#     print("I like you!");
# else:
#     print ("Get out of here")
# print("###############################################")
#
#
#
# with open("courses.txt") as courses_file: # чтобы открыть файл COURSES.txt в переменной courses_file
#     for line in courses_file:
#         print(line)





