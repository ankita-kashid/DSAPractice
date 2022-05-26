# https://leetcode.com/problems/two-out-of-three/

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        a=set(nums1+nums2+nums3)
        
        ans=[]
        for i in a:
            if i in nums1 and i in nums2:
                ans.append(i)
            elif i in nums2 and i in nums3:
                ans.append(i)
            elif i in nums1 and i in nums3:
                ans.append(i)
            else:
                continue
        print(ans)
        return ans
