class Solution:
    def isValid(self, s: str) -> bool:
        seen = []

        for ele in s:
            if ele == ')':
                if seen and seen.pop() == '(':
                    continue
                else:
                    return False
            elif ele == '}':
                if seen and seen.pop() == '{':
                    continue
                else:
                    return False
            elif ele == ']':
                if seen and seen.pop() == '[':
                    continue
                else:
                    return False
            else:
                seen.append(ele)

        if not seen:
            return True
        else:
            return False

        