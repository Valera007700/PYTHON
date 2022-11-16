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

from ctypes.wintypes import FLOAT


childs_meal = input ("What is the price of a child's meal?  ");
adults_meal = input ("What is the price of an adult's meal?  ");

many_children = input ("How many children are there?  ");
many_adults = input ("How many adults are there?  ");

tax_rate = input ("What is the sales tax rate?")
childs = (float(childs_meal)) * (float(many_children))
adults = (float(adults_meal)) * (float(many_adults))
subtotal = (float(childs)) + (float(adults));
sales_tax = ((float(subtotal)) * (int(tax_rate)) / 100)
total = sales_tax + subtotal





print ("Subtotal: ", subtotal)
print ("Sales Tax: ", sales_tax)
print ("Total: ", total)

payment  = input ("What is the payment amount?  ");
change = ((int(payment)) - total)
change_2 = round(change, 2)
print("Change: " ,change_2)


#print (int(firts_num) + int(second_num))
