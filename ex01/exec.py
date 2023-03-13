import sys
final_string = ''

for i in range (1, len(sys.argv)):
    final_string += sys.argv[i] + ' '
print(final_string.rstrip().swapcase()[::-1])
