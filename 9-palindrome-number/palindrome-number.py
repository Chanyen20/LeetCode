class Solution:
    def isPalindrome(self, x: int) -> bool:
        listA = list(str(x))
        # listA_reverse = listA.reverse()
        if listA == listA[::-1]:
            return True
        else:
            return False
        