#3.
#inp = "abcdefgh"
#out = "aB12cD23eF34gH45"

inp = "abcdefgh"
out = ""
count,c1 = 0,1

for i in range(len(inp)):
    if count == c1:
        out = out + inp[i].upper() + str(c1) + str(c1+1)
        c1 = c1 + 1
    else:
        out = out + inp[i]
        count += 1
print(out)