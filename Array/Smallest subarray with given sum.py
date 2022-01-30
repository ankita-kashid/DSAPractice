"""
arr[] = {1, 4, 45, 6, 0, 19}
   x  =  51
Output: 3
Minimum length subarray is {4, 45, 6}
"""

def smallest(nums,x):
    dic={}
    prefix=0
    count=1000000
    for i in range(len(nums)):
        prefix+=nums[i]
        dic[prefix]=i
 
    print(dic)
    prefix=0
    for i in range(len(nums)):
        prefix+=nums[i]
       # print(prefix,prefix-x)
        if prefix-x in dic:
            
            start=dic[prefix-x]
            end=dic[prefix]
            #print(start,end,"f")
            count=min(count,end-start)
    return count

print(smallest([1, 10, 5, 2, 7],9))