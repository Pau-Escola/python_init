import sys
res = 0;
if (len(sys.argv) == 3):
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print ("Sum:        " + str(a + b))
        print ("Difference: " + str(a - b))
        print ("Product:    " + str(a * b))
        if (b == 0):
            print ("Quotient:   ERROR (division by 0)")
            print ("Remainder:  ERROR (module by 0)")
        else:
            print ("Quotient:   " + str(a / b))
            print ("Remainder:  " + str(a % b))
    except:
        print ("Not recognized as nummber")
else:
    print ("Wrong number of args")
