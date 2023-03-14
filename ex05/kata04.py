kata = (0, 4, 132.422222, 10000, 12345.67)

ans1 = "module_" + '{:0>2}'.format(kata[0])
ans2 = "ex_" + str('{:0>2}'.format(kata[1]) + " : " + str('{:.2f}'.format(kata[2])))
ans3 = "{:.2e}".format(kata[3])
ans4 = "{:.2e}".format(kata[4])
print(ans1 + ", " + ans2 + ", " + ans3 + ", " + ans4)
