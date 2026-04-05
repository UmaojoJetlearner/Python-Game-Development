import random

secretset=set()

while len(secretset)<5:
    num=random.randint(1,20)
    secretset.add(num)
guessedset=set()
print(" Welcome to guess the scret set game, enjoy! \n Guess the number from 1 through 20") 
while guessedset != secretset:
    guess=int(input("Enter your guess!"))