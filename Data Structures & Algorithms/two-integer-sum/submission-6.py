class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}
        for j,x in enumerate(nums):
            if target - x in seen:
                return [seen[target - x], j]
            seen[x] = j