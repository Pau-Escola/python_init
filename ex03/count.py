import string

def text_analyzer(*args):
    p = ''
    if(len(args) > 1):
        print ("Too many arguments")
    elif (len(args) == 0):
        while (not p):
            p = input("What should I do next? ")
    else:
        p = args[0]
    try:
        p = int(args[0])
        print("Argument provided is not a String.")
        #for i in range(0, len(s) - 1):
            #t = s[i];
            #if (t.isupper()):
             #   upper_l += 1
            #elif(t.islower()):
            #    lower_l += 1
           # elif(t == " "):
          #      spaces += 1
          #  else:
         #       punc_mark += 1
        #printf ("Lower letters: %i \n Caps: %i", lower_l, upper_l)
    except:
        print("Argument provided is a String.")
        s = str(p)
        upper_l = 0
        lower_l = 0
        spaces = 0
        punc_mark = 0
        chars = 0
        for i in range(0, len(s)):
            t = s[i]
            if (t.isupper()):
                upper_l += 1
            elif(t.islower()):
                lower_l += 1
            elif(t == " "):
                spaces += 1
            elif(t in string.punctuation):
                punc_mark += 1
            chars = i;
        print ("Total characters: " + str(chars + 1) + ".\n" + "Lower letters: " + str(lower_l) +".\n" + "Upper letters: " + str(upper_l) + ".\n" + "Spaces: " + str(spaces) + ".\n" + "Punctuation mark: " + str(punc_mark) + ".")
