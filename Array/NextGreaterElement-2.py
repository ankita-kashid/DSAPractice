"""
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
"""

def great(nums):
    res=[-1]*len(nums)
    n=len(nums)
    stack=[]
    size=n+(n-1)
    for i in range(size):
        idx=i%n
        while len(stack)>0 and nums[idx]>stack[-1][1]:
            a,b=stack.pop()
            res[a]=nums[idx]
        stack.append([idx,nums[idx]])
    return res
        






if __name__=='__main__':
    nums=[5,4,3,2,1]
    print(great(nums))