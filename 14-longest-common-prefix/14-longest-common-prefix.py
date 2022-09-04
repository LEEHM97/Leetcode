class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        min_length = min(strs, key=len)
        
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
