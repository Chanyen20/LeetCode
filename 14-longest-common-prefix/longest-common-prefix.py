class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs_order = sorted(strs)

        first = strs_order[0]
        last =  strs_order[-1]
        length = min(len(first), len(last))
        for i in range(length):
            if first[i] != last[i]:
                return first[:i]
        
        return first


        