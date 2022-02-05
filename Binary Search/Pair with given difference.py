"""
Input:
L = 6, N = 78
arr[] = {5, 20, 3, 2, 5, 80}
Output: 1
Explanation: (2, 80) have difference of 78.
"""
def pair(nums,x):
    nums.sort()
    for i in nums:
        target=i+x
        ans=search(nums,target)
        if ans!=1:
            return [nums[ans],i]

def search(nums,target):
    start=0
    end=len(nums)-1
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            end-=1
        else:
            start+=1
    return -1

print(pair([5, 20, 3, 2, 5, 80],78))
            