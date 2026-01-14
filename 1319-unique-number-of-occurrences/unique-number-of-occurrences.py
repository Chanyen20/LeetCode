class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = {}

        for num in arr:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        
        return len(seen) == len(set(seen.values()))


        