class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
          if s[i]!=s[j]:
            right=s[i:j]
            left=s[i+1:j+1]
            return right==right[::-1] or left==left[::-1]
          i+=1
          j-=1
        return True