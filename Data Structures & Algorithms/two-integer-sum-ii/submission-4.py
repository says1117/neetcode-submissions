class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        res = []
        
        while target != numbers[i] + numbers[j]:
            if target > numbers[i] + numbers[j]:
                i+=1
            if target < numbers[i]+numbers[j]:
                j-=1
        res.append(i+1)
        res.append(j+1)
        return res