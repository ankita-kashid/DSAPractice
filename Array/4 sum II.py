"""
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
"""
def sum4(a,b,c,d):
    dic={}
    count=0
    for i in range(len(a)):
        for j in range(len(b)):
            dic[a[i]+b[j]]=1

    for i in range(len(c)):
        for j in range(len(d)):
            target=-(c[i]+d[j])
            if target in dic:
                count+=dic[target]
    return count





print(sum4([1,2],[-2,-1],[-1,2],[0,2]))