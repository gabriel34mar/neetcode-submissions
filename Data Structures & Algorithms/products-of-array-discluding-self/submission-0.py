class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr=[1]*len(nums)
        acumi=1
        acumd=1
        for e,n in enumerate(nums):
            arr[e]=arr[e]*acumi
            acumi=acumi*n

        for e in range(len(nums)-1,-1,-1):
            arr[e]=arr[e]*acumd
            acumd=acumd*nums[e]
    
        return arr


            
