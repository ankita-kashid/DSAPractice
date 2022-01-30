"""
[4,5,6,7,0,1,2], target = 0
"""
def search(nums,t):
    start=0
    end=len(nums)-1
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==t:
            return mid
        elif nums[start]<=nums[mid]:
            if nums[mid]>t and nums[start]<=t:
                end=mid-1
            else:
                start=mid+1
        else:
            if nums[mid]<t and nums[end]>=t:
                start=mid+1
            else:
                end=mid-1
    return -1

print(search([4,5,6,7,0,1,2],9))
        
