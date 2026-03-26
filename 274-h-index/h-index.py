class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # n = len(citations)
        # counter = n
        # citations.sort()

        # for i in range(n):
        #     if citations[i] >= n - i:
        #         return n - i
        # return 0
        citations.sort()
        total = len(citations)

        for i, num in enumerate(citations):
            rest_num = total - i
            if num >= rest_num:
                return rest_num
        return 0

        
            



        
        