class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp = set(nums)

        if len(nums) != len(tmp):
            return True
        return False