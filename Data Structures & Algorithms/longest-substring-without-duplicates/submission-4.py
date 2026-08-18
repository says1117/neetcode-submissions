class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        res = 0

        for right, char in enumerate(s):
            # last_seen[char] >= left means that we have not viewed this substring combination yet
            # if last_seen[char] is <= left that means this sequence has been exhausted will mess up out answer because we would be checking
            # a possibility in the past
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            last_seen[char] = right

            res = max(res, right-left+1)
        return res