import random

number_to_guess = random.randint(1,99)
print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!""")
ans = ''
tries = 0
while not (ans == str(number_to_guess)):
    tries += 1
    print("Guess")
    ans = input()
    if (ans == "exit"):
        break
    if (not ans.isdigit()):
        print("You have to input a number between 1 and 99")
    elif (int(ans) > number_to_guess and int(ans) < 100):
        print("Lower!")
    elif (int(ans) < number_to_guess and int(ans) > 0):
        print("Higher!")
    elif(int(ans) > 99 or int(ans)< 1):
        print("The number is between 1 and 99")
    elif(int(ans) == number_to_guess):
        if (ans == "42"):
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if (tries == 1):
            print("On the first try, wow!")
        print("Awesome!")
        if (tries > 1):
            print("You got it in " + str(tries) + " tries!")
        break
        
