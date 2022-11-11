# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         Solution 1 using ZIP
#         match = 0
        
#         for vals in zip(*strs):
#             if len(set(vals)) == 1:
#                 match += 1
#             else:
#                 break
        
#         return strs[0][:match]

# Solution 2

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(1,len(strs[0])+1):
            for j in range(1,len(strs)):
                s = strs[0][:i]
                if strs[j][:i] != s:
                    return strs[0][:i-1]
        return strs[0]



