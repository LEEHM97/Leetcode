class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        i = 0
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        while i < len(s):
            if i == len(s)-1:
                answer += roman_dict[s[i]]
                break
            else:
                if s[i] == 'I' and s[i+1] == 'V':
                    answer += 4
                    i += 2
                elif s[i] == 'I' and s[i+1] == 'X':
                    answer += 9
                    i += 2
                elif s[i] == 'X' and s[i+1] == 'L':
                    answer += 40
                    i += 2
                elif s[i] == 'X' and s[i+1] == 'C':
                    answer += 90
                    i += 2
                elif s[i] == 'C' and s[i+1] == 'D':
                    answer += 400
                    i += 2
                elif s[i] == 'C' and s[i+1] == 'M':
                    answer += 900
                    i += 2
                else:
                    answer += roman_dict[s[i]]
                    i += 1
                    
        return answer