class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #  Ensure that the charctor in magazine is enough
        if len(magazine) < len(ransomNote):
            return False

        seen_magazine = dict()

        for char in magazine:
            if char in seen_magazine:
                seen_magazine[char] += 1
            else:
                seen_magazine[char] = 1
        
        for char in ransomNote:
            if char in seen_magazine:
                seen_magazine[char] -= 1

                if seen_magazine[char] < 0:
                    return False
            else:
                return False
        return True
        