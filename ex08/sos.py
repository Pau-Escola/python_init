import sys

MORSE_CODE_DICT = { 
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
    ', ':'--..--',
    '.':'.-.-.-',
    '?':'..--..',
    '/':'-..-.',
    '-':'-....-',
    '(':'-.--.',
    ')':'-.--.-'
    }

word_to_translate = ''
word_translated = ''

if (len(sys.argv) > 1):
    #try:
    for i in range (1, len(sys.argv)):
        word_to_translate += sys.argv[i] + ' '
    word_to_translate = word_to_translate.rstrip().upper()
    for i in range(0, len(word_to_translate)):
        if word_to_translate[i] == ' ':
            word_translated += '/'
        else:
            word_translated += MORSE_CODE_DICT[word_to_translate[i]]
    print (word_translated)
    #except:
      #  print("ERROR")
else:
    print("You nedd to pass an argument")


