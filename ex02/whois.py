import sys

if (len(sys.argv) == 2):
    if (sys.argv[1].isdigit()):
        if (int(sys.argv[1]) == 0):
            print("I am Zero.")
        elif (int(sys.argv[1]) / 2 == 1 or int(sys.argv[1] == 1)):
            print("I am Odd.")
        else:
            print("I am Even.")
    else:
        print ("AssertionError : argument is not an integer")
elif (len(sys.argv) > 2):
    print ("AssertionError: more than one argument are provided")
else:
    print ("AssertionError: no argument provided")
