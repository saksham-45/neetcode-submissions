class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # from first element compare all other since its common for all strings in array we must at each instance get the same first
        # values if it dont happen and the ans string empt return it but concatante the ans string progressively
        nex=0
        res=""
        min_string = min(strs, key=len)
        min_length = len(min_string)
        if not strs:
            return res

        for j in range(min_length):
            for i in range(len(strs)):
              while strs[0][j]!=strs[i][j]:
                return res
            res+=strs[0][j]
        return res
               


