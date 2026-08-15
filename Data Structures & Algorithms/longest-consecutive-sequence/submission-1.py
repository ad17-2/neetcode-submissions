class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        streak = 0

        for num in nums:

            if num - 1 not in num_set:
                #start of seq
                curr = num
                curr_streak = 1
                while curr + 1 in num_set:
                    curr_streak += 1
                    curr += 1
                #break loop if curr + 1 not found, find longest streak

                streak = max(streak, curr_streak)

        return streak