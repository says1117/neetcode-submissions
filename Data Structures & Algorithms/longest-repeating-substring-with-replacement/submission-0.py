class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        res = 0
        maxf = 0
        for r, curChar in enumerate(s):
            count[curChar] = 1 + count.get(curChar, 0)
            maxf = max(maxf, count[curChar])

            while (r-left + 1) - maxf > k:
                count[s[left]] -=1
                left+=1
            res = max(res, r - left + 1)

        return res