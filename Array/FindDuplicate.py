#Find the duplicate without modifying the array in constant extra space and only one number is 
# duplicate in the given array and values in the array should be between [1,n-1
# ]

def dupli(nums):
    slow=nums[0]
    fast=nums[nums[0]]
    while fast!=slow:
        slow=nums[slow]
        fast=nums[nums[fast]]

    fast=0
    while fast!=slow:
        slow=nums[slow]
        fast=nums[fast]
    return slow




if __name__=="__main__":
    print(dupli([1,2,3,3,4]))