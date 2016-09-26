import random
BOUNDS = (1, 100)
TRIES_ALLOWED = 10
number = random.randint(*BOUNDS)
seguir = bool(True)
while seguir == True:
    print("Welcome to 'Guess a Number'!\n")
    print("I think a number from %d to %d." % BOUNDS)
    print("You will try to guess in the fewest possible attempts, are you ready?\n")
    for tries in range(TRIES_ALLOWED):
        try:
            print tries
            guess = int(input("Take a number: "))
            if guess > number:
                print("Too High...\n")
            elif guess < number:
                print("Too Low...\n")
            else:
                print("\nYou guessed it! The number was %d\n" % (number))
                print("And it only took you %d tries!\n" % (tries + 1))
                print("Congratulations!\n")
                try:
                    print("\nYou want to play again?")
                    answer = raw_input("Write your answer here: \n")
                    if answer == "Yes":
                        break
                    elif answer == "No":
                        seguir = False
                        break
                    else:
                        print("\nOnly 'Yes' or 'No'")
                except:
                    print("Error, sorry, contact management!")
                    seguir = False
                    break
        except:
            print("Care only enter numbers!\n")
            print("The error is taken as a shift!\n")
    else:
        print("You have failed all your attempts!")
        print("The number was: "), number
        while seguir == True:
            try:
                print("\nYou want to play again?")
                answer = raw_input("Write your answer here: \n")
                if answer == "Yes":
                    break
                elif answer == "No":
                    seguir = False
                    break
                else:
                    print("\nOnly 'Yes' or 'No'")
            except:
                print("Error, sorry, contact management!")
                seguir = False
                break
    try:
        input("\nPress enter to play if you choose 'Yes' or exit if you choose 'No'!\n")
    except:
        pass
