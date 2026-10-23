class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        brute force: 2 loops going through n letters in list, take 1 number i, compare with all numbers j except itself. needs to enumerate and check (using in range(0, nums)). check to see if idx ==, if it is then skip

        optimal: set take in all numbers, if num in set, true. outside of loop return false since there will be duplicate
        '''

        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False