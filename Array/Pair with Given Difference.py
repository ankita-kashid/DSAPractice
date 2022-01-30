"""
Input:
L = 6, N = 78
arr[] = {5, 20, 3, 2, 5, 80}
Output: 1
Explanation: (2, 80) have difference of 78.
"""
def pair(nums,x):
    dic={}
    count=0
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]]=1
        else:
            dic[nums[i]]+=1
    l=[]
    for i in range(len(nums)):
        if x+nums[i] in dic:
            count+=dic[x+nums[i]]
            l.append([x+nums[i],nums[i]])
    return l

print(pair( [1,2,3,4,5],1))
