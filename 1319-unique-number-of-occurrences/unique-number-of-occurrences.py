class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()

        cnt = 0
        seen_cnt = set()

        for i in range(len(arr)):
            if i == 0:
                cnt += 1
                continue
            
            if arr[i] == arr[i - 1]:
                cnt += 1
            else:
                if cnt in seen_cnt:
                    return False
                seen_cnt.add(cnt)
                cnt = 1
            
        if cnt in seen_cnt:
            return False
        return True
        


        