class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for ch in s:
            if ch.isalnum():
                st+=ch
        if st.casefold()==st[::-1].casefold():
            return True
        return False
        

        
            
            
                