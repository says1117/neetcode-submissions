class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        res = 0

        for right, char in enumerate(s):
            # last_seen[char] >= left means the previous occurrence of this char
            # is still inside our current window -> it's a live duplicate,
            # so left must jump past it.
            #
            # last_seen[char] < left means the previous occurrence is already
            # outside our current window (we trimmed past it earlier) -> stale,
            # safe to ignore.
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            last_seen[char] = right

            res = max(res, right-left+1)
        return res