def fourSum(nums, target):
		nums.sort()
		l=[]
		for i in range(len(nums)):
			for j in range(i+1,len(nums)):
				k=i+1
				r=len(nums)-1
				while k<r:
					total=nums[i]+nums[j]+nums[k]+nums[r]
					if total==target:
						res=[nums[i],nums[j],nums[k],nums[r]]
						if res not in l:
							l.append(res)
					elif total>target:
						k+=1
					else:
						r-=1
		return l
nums=[ 9, -8, -10, -7, 7, -8, 2, -7, 4, 7, 0, -3, -4, -5, -1, -4, 5, 8, 1, 9, -2, 5, 10, -5, -7, -1, -6, 4, 1, -5, 3, 8, -4, -10, -9, -3, 10, 0, 7, 9, -8, 10, -9, 7, 8, 0, 6, -6, -7, 6, -4, 2, 0, 10, 1, -2, 5, -2 ]
print(fourSum(nums,0))