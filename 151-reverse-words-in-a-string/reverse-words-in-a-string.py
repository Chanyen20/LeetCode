class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = []
        pointer = len(words) - 1

        while pointer >= 0:
           res.append(words[pointer])
           pointer -= 1
        
        return ' '.join(res)


        
      
        