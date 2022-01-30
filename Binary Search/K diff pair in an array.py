#https://leetcode.com/problems/k-diff-pairs-in-an-array/
"""
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

"""

def findPairs(nums,x):
    dic={}
    count=0
    idx=0
    nums.sort()
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]]=i
            idx=search(nums[i+1:],x+nums[i])
            if idx!=-1:
                count+=1
    return count

def search(nums,t):
    start=0
    end=len(nums)-1
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==t:
            return mid
        elif nums[mid]>t:
            end=mid-1
        else:
            start=mid+1
    return -1

print(findPairs([3,1,4,1,5],2))




