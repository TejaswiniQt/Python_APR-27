#2.  
#inp = "abcdefgh"
#out = "abCdeFgh"

inp = "abcdefghijklm"
out = ""
count = 2

for i in range(len(inp)):
    if count == i:
        out = out + inp[i].upper()
        count+=3
    else:
        out = out + inp[i]
print(out)