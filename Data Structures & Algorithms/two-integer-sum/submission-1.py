class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        num_list = [i, j]
                        if num_list[0] < num_list[1]:
                            return num_list
                else:
                    continue


        return num_list