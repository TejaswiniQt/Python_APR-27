 #5. WAP to find the maximun length of consecutive 0's in a binary string
 
 
inp = "0100010100010010000100100"
count = 0
max_count = 0
strt_index = 0
cnt = 0
st_index = 0


for i in range(len(inp)):
    if int(inp[i]) == 0:
        count += 1 
        if count == 1:
            st_index = i
    else:
        if max_count < count:
            max_count = count
            strt_index = st_index
        count = 0
        
if max_count < count:
    max_count = count
    strt_index = st_index
        
        
print("Length of consecutive 0's is : {}".format(max_count))
print("Starting index is : {}".format(strt_index))

