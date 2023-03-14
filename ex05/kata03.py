import sys

kata = "The right format"
ans = ''
if (len(kata) < 42):
    for i in range (0, 41 - len(kata)):
        ans += '-'
    ans += kata
sys.stdout.write(ans)
