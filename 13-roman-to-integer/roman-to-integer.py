class Solution:
    def romanToInt(self, s: str) -> int:
        roman_mapping = {'I': 1,'V': 5, 'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        total = 0

        for i in range(1, len(s)):
            if roman_mapping[s[i - 1]] >= roman_mapping[s[i]]:
                total +=  roman_mapping[s[i - 1]]
            else:
                total -=  roman_mapping[s[i - 1]]
        
        total += roman_mapping[s[-1]]

        return total




