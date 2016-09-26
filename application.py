import random
BOUNDS = (1, 100)
TRIES_ALLOWED = 10
number = random.randint(*BOUNDS)
seguir = bool(True)
while seguir == True
    print("Welcome to 'Guess a Number'!\n")
    print("I think a number from %d to %d." % BOUNDS)
    print("You will try to guess in the fewest possible attempts, are you ready?\n")
    for tries in range(TRIES_ALLOWED):
        guess = int(input("Take a number: "))
        if guess > number:
            print("Too High...\n")
        elif guess < number:
            print("Too Low...\n")
        else:
            print("\nYou guessed it! The number was %d\n" % (number))
            print("And it only took you %d tries!\n" % (tries + 1))
            print("Congratulations!\n")
            break
    else:
        print("You have failed all your attempts!")
        print("The number was: "), number
    try:
        input("\nPress enter to exit.\n")
    except:
        pass
