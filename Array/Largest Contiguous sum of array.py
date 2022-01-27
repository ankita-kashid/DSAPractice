"""
nums=[-2, -3, 4, -1, -2, 1, 5, -3]
"""
import math


def contiguous(nums):
    final=-1000000
    curr_sum=0

    for i in range(0,len(nums)):
        curr_sum=curr_sum+nums[i]
        #print(curr_sum,end=" ")
        if final<curr_sum:
            final=curr_sum

      
    return final

print(contiguous([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]))