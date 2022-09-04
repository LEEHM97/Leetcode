class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        min_length = strs[0]
        for i in range(1, len(strs)):
            if len(min_length) > len(strs[i]):
                min_length = strs[i]
        
        if len(strs) == 1:
            return strs[0]
        
        alph = 0
        
        while alph<len(min_length):
            for i in range(len(strs)-1):
                if strs[i] == "":
                    return ""
                if strs[i][alph] != strs[i+1][alph]:
                    return answer
            answer += strs[0][alph]
            alph += 1
            
        return answer
