"""
Input: nums = [3,2,1,5,6,4], k = 2
Output: 2
"""

def largest(nums,k):
    pivot= nums[0]
    left = [x for x in nums if x < pivot]
    mid=[x for x in nums if x==pivot]
    right=[x for x in nums if x > pivot]

    L,M=len(left),len(right)
    if k < L:
        return largest(left,k)
    elif k>(L+M):
        return largest(right,(k-(L+M)))
    else:
        return mid[0]


if __name__=='__main__':
    nums=[3,2,1,0,6,4]
    k=4
    print(largest(nums,k))