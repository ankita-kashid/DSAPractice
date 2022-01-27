"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers.
Assume that there will only be one solution
Example: 
given array S = {-1 2 1 -4}, 
and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
"""
def threesumclosest(nums,t):
    diff=1000000
    nums.sort()
    for i in range(len(nums)):
        l=i+1
        r=len(nums)-1
        while l<r:
            s=nums[i]+nums[l]+nums[r]
            if abs(s-t)<diff:
                res=s
                diff=abs(s-t)
            if s==t:
                return s
            if s>t:
                r-=1
            else:
                l+=1
    return res
print(threesumclosest([-1,2,1,-4],1))
