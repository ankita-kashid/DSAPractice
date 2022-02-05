#https://leetcode.com/problems/container-with-most-water/

"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""
def container(nums):
    start=0
    end=len(nums)-1
    area=0
    while start<end:
        height=min(nums[start],nums[end])
        area=max(area,height*(end-start))
        if nums[start]<nums[end]:
            start+=1
        else:
            end-=1
    return area

print(container([1,8,6,2,5,4,8,3,7]))