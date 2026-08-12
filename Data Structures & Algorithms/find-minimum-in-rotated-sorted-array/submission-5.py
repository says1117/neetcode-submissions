class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]
        while l <= r:
            m = (l+r) // 2
            res = min(res, nums[m])
            res = min(res, nums[l])
            if nums[l] <= nums[m]:
                l = m+1
            else:
                r = m-1
        return res

        
