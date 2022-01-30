"""
nums=[1, 1, 1,2, 2, 2, 2, 3]
x=2
"""
def counts(nums,x):
    n=len(nums)
    start=0
    end=n-1
    while start<end:
        mid=(start+end)//2
        if nums[mid]==x:
            return mid
        elif nums[mid]>x:
            end=mid-1
        else:
            start=mid+1
    return -1

def occurences(nums,x):
    idx=counts(nums,x)
    if idx==-1:
        return 0
    count=1
    left=idx-1
    while left>0 and nums[left]==x:
        count+=1
        left-=1
    
    right=idx+1
    while right< len(nums) and nums[right]==x:
        count+=1
        right+=1
    return count

print(occurences([1,1,2,2,2,2,3],2))
    
