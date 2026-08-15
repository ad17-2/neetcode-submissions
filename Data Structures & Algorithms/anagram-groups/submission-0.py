class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for item in strs:
            sortedItem = ''.join(sorted(item))
            res[sortedItem].append(item)

        return list(res.values())