class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for item in strs:
            sorted_item = ''.join(sorted(item))
            res[sorted_item].append(item)

        return list(res.values())