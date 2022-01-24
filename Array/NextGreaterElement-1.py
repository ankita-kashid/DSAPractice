"""
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
"""
def great(nums1,nums2):
    h={}
    res=[]
    stack=[]
    for num in nums2:
        while len(stack)>0 and num>stack[-1]:
            h[stack.pop()]=num
        stack.append(num)

    for num in nums1:
        if num in h:
            res.append(h[num])
        else:
            res.append(-1)
    return res




if __name__=='__main__':
    nums1=[4,1,2]
    nums2=[1,3,4,2]
    print(great(nums1,nums2))