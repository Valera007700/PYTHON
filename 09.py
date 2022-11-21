
print('Welcome to the Shopping Cart Program!')
print()
cart = []
prices = []
select = 0
while( select != 5):
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    print()
    select = int(input('Please select one of the following: '))
    print()
    if (select > 5 or select < 1):
        print('Ooops... Try again:)')
    if select == 1:
        item = input('What item would you like to add? ')
        cart.append(item)
        price = float(input(f'What is the price of {item}? '))
        prices.append(price)
        print(f'{item} for ${price} has been aded to the cart.')
        print()

    elif select == 2:
        print('The contents of the shopping cart are: ')
        print('-' * 15)
        for i in range(len(cart)):
            print(f"{i + 1}.{cart[i]} -- ${prices[i]}")
        print('-' * 15)
    

    elif select == 3:
        item = int(input('Which item would you like to remove? '))
        item -= 1
        count = len(prices)
        if item > count or item < 0:
            print ('Item not in list. Try again')
        else:
            thing = cart[item]
            cart.pop(item)
            prices.pop(item)
            print(f'{thing} has been removed from the list.')
            print()


    elif select == 4:
        sum = 0
        for price in prices:
            sum += price 
        print('-' * 15)
        print(f'The total price of the items in the shopping cart is {sum:.2f} ')
        print()


    elif select == 5:
        print('Thank you. Have a good day. Goodbye.')