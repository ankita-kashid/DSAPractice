"""
 arr = [10, 2, -2, -20, 10]
 sum=-10
"""
def number(nums,t):
    dic={}
    prefix=0
    count=0
    for i in range(len(nums)):
        prefix+=nums[i]

        if prefix==t:
            count+=1
        if prefix-t in dic:
            count+=dic[prefix-t]
        if prefix in dic:
            dic[prefix]+=1
        else:
            dic[prefix]=1
        
    print(dic)
    return count
print(number([1,2,3],3))


