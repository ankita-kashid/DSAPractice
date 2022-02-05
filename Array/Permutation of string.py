s="abc"
for i in range(len(s)):
    ch=s[i]
    left=s[0:i]
   # print(left,"left",i,"i")
    right=s[i+1:]
    #print(right,"right",i,"i")
    rest=left+right
    #print(rest,"rest",i,"i")
    
    print(rest,left,right)