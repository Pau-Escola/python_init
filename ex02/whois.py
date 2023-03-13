import sys

if (len(sys.argv) == 2):
    try:
        n = int(sys.argv[1]);
        print ("I am Zero.") if n == 0 else print("I am Odd.") if n % 2 == 1 or n == 1 else print("I am Even.")
    except:
        print ("AssertionError : argument is not an integer")
elif (len(sys.argv) > 2):
    print ("AssertionError: more than one argument are provided")
else:
    print ("AssertionError: no argument provided")
