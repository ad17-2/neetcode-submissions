class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tmp = Counter(nums)
        sorted_by_freq = sorted(tmp.items(), key=lambda x: x[1], reverse=True)
        items = sorted_by_freq[0:k]
        top_2_keys = [key for key, _ in items]
        return top_2_keys
