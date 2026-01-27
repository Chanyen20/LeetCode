class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False


        seen_pattern = dict() #["p": "word"]
        seen_words = dict()   #["word": "p"]

        for p, w in zip(pattern, words):
            if p in seen_pattern and  w != seen_pattern[p]:
                return False
            
            if w in seen_words and  p != seen_words[w]:
                return False

            seen_pattern[p] = w
            seen_words[w] = p
        
        return True


        