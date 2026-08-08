class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        top = 0

        for i in res:
            seq = 1
            if i-1 not in res:
                cur = i
                while (cur + 1) in res:
                    seq +=1
                    cur +=1
            if seq > top:
                top = seq
            
        return top