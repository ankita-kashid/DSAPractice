"""
[4,5,6,7,0,1,2], target = 0
"""
def search(nums,t):
    start=0
    end=len(nums)-1
    while start<end:
        mid=(start+end)//2
        if start<mid<end and nums[mid]==t:
            return mid
        





print(search([4,5,6,7,0,1,2],0))