#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
"""

def twosum(nums,t):
    for i in range(len(nums)):
        new=t-nums[i]
        start,end=i+1,len(nums)-1

        while start<=end:
            mid=(start+end)//2
            if nums[mid]==new:
                return [i+1,mid+1]
            elif nums[mid]>new:
                end=mid-1
            else:
                start=mid+1

if __name__=='__main__':
    nums=[2,7,11,15]
    target=9
    print(twosum(nums,target))