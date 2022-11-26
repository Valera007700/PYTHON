for number in range(1, 9):
    print(number)


for number in range(2,21,2):
    print(number)



word = input('Input your word : ')
letterf = input('What is your favorite letter? ')
for letter in word:
    if letter.lower() == letterf.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

for letter in word:
    if letter.lower() == letterf.lower():
        print("_",end="")
    else:
        print(letter.lower(), end="")
print()


nelson = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
#letterf = input("What is your favorite letter? ")
n_number = int(input("Write number of n-th letter: "))

for i, letter in enumerate(nelson):
    if i % n_number == 0:
        print(letter.upper(), end="")
    else:
        print(letter.lower(),end="")