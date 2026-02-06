class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_strs = dict()

        for word in strs:
            word_key = str(sorted(word))

            if word_key in group_strs:
                group_strs[word_key].append(word)
            else:
                group_strs[word_key] = [word]
        
        return list(group_strs.values())
        