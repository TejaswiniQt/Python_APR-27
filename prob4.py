#4:
#inp = "a2b3c4"
#out = exp_out = "aabbbcccc"


inp = "a2b3c4d5"
out = ""

for i in range(0,len(inp),2):
    print(inp[i]*int(inp[i+1]),end="")