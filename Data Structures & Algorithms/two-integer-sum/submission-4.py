class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        befMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in befMap:
                return [befMap[diff], i]
            befMap[n] = i
        return
