# https://leetcode.com/problems/smallest-index-with-equal-value/

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        ans=[]
        
        for i in range(len(nums)):       
            if i % 10 == nums[i]:
                ans.append(i)
            else:
                continue
        
       
        if len(ans)==0:
            return -1
        else:
            return min(ans)
