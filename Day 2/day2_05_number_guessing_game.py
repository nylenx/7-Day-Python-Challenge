import random

answer = random.randint(1,13)
not_guessed = True
print("Guess between 1 to 13")
while(not_guessed):
    guess = int(input('Guess genius =>'))

    if answer == guess:
        print("JACKPOT! you nailed it")
        not_guessed = False
    else:
        print("OOPs no, Guess again!")

