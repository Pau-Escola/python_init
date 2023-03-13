import string

def text_analyzer(*args):
    if(len(args) == 1):
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
            s = args[0]
            upper_l = 0
            lower_l = 0
            spaces = 0
            punc_mark = 0
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
            print ("Lower letters: " + str(lower_l) +".\n" + "Upper letters: " + str(upper_l) + ".\n" + "Spaces: " + str(spaces) + ".\n" + "Punctuation mark: " + str(punc_mark) + ".")
