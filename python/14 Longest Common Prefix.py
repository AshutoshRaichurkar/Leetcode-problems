## Leetcode Link: https://leetcode.com/problems/longest-common-prefix/description/
## Solution Link: https://www.youtube.com/watch?v=jzZsG8n2R9A

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i== len(s) or s[i] != strs[0][i]:
                    return res   
            res+= strs[0][i]
        return res
