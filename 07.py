secret = 'mosiah'

guess = input('What is your guess? ')
guess = guess.lower()

count = 1
while(secret != guess):
    print('Wrong.Try again.')
    guess = input('What is your guess? ')
    guess = guess.lower()
    count += 1




print('Yay,you guessed right!')
print(f'You did {count} tries')
secret = 'mosiah'
mask =''
count = 1

for i in secret:
    mask = mask + '_ '
print(f'Your hint is: {mask}')

guess = input('What is your guess? ')
guess = guess.lower()

while (secret != guess):
    letter = '_ '
    mask = ''
    for i, j in enumerate(guess):

        for a, k in enumerate(secret):

            if (i == a and j == k):
                letter = j.capitalize() + ' '
            elif ( j == k):
                letter = a + ' '
        mask = mask + letter

    print(f'Your hint is: {mask}')
    guess = input('What is your guess? ')
    guess = guess.lower()
    count += 1

print('Yay,you guessed right!')
print(f'You did {count} tries')