
def longest(nums):
    dic={}
    ans=0
    start=0
    for i in range(len(nums)):
        print(dic,start,ans)
        if nums[i] in dic:
            start=max(start,dic[nums[i]]+1)
        #else:
        ans=max(ans,i-start+1)
        dic[nums[i]]=i
    return ans

print(longest("geeksforgeeks"))