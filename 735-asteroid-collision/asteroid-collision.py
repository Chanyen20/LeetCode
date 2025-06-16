class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for element in asteroids:
            while res and element < 0 < res[-1]:
                if abs(res[-1]) < abs(element):
                    res.pop()
                    continue
                elif abs(res[-1]) == abs(element):
                    res.pop()
                break     
            else:
                res.append(element)
        return res

# time: O(n)
# space: O(n)
        