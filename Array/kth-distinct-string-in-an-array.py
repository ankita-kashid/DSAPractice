# https://leetcode.com/problems/kth-distinct-string-in-an-array/

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans=[]
        for i in arr:
            if arr.count(i)==1:
                ans.append(i)
        
        #print(ans[k-1])
        if len(ans)<k:
            return ""
        else:
            return ans[k-1]
        #return ans[k-1]
        
