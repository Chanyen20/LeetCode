class Solution:
    def isHappy(self, n: int) -> bool:
        prev = str(n)
        seen = set()

        while prev != "1":
            curr_sum = 0
            for num in prev:
                curr_sum += int(num) ** 2
            
            if curr_sum in seen:
                return False

            seen.add(curr_sum)
            prev = str(curr_sum)

        return True

        