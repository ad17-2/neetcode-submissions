class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_num = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in seen_num:
                return [seen_num[diff], i]
            seen_num[n] = i