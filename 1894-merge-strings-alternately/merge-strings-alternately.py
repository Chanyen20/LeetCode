class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = [] 
        i = 0
        j = 0

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])

            i += 1
            j +=1 
        
        # Append the remaining character of the word
        result.append(word1[i:])
        result.append(word2[j:])

        return ''.join(result)

# time complexity: O(n + m)  ; n = len(word1), m = len(word2)
# space complexity: O(n + m)  ; n = len(word1), m = len(word2)

        