class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0

        n = len(word1)
        m = len(word2)

        result = ""

        while i < n and j < m:
            result += word1[i]
            i += 1
            result += word2[j]
            j += 1

        while i < n:
            result += word1[i]
            i += 1
        
        while j < m:
            result += word2[j]
            j+=1
        
        return result