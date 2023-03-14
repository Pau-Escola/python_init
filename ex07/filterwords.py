import sys

if (len(sys.argv) == 3):
    try:
        words = sys.argv[1].split(' ')
        words_ans = list()
        for word in words:
            if len(word) > int(sys.argv[2]):
                words_ans.append(word)
        print (words_ans)
    except:
        print("The second argument must be an int")
else:
    print("Not the right number of arguments")