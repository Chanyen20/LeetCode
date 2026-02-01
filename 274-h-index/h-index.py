class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counter = n
        citations.sort()

        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0
        
            



        
        