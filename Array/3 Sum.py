"""
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""
def sum3(nums):
    out=[]
    nums.sort()
    for i in range(len(nums)):
        l=i+1
        r=len(nums)-1
        x=nums[i]
        while l<r:
            if x+nums[l]+nums[r]==0:
                res=[x,nums[l],nums[r]]
                if res not in out:
                    out.append([x,nums[l],nums[r]])
                l+=1
                r-=1
            elif x+nums[l]+nums[r] <0:
                l+=1
            else:
                r-=1
    return out if len(out) else []
                
            




print(sum3([-1,0,1,2,-1,-4]))