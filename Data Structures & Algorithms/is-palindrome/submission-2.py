class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for ch in s:
            if ch.isalnum():
                st+=ch.lower()
        if st==st[::-1]:
            return True
        return False
        

        
            
            
                