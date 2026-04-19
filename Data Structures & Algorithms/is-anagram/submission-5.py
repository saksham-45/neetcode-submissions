class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dick={}
        dick2={}
        ss=len(s)
        tt=len(t)
        for i in s:
            dick[i]=dick.get(i,0)+1
        for j in t:
            dick2[j]=dick2.get(j,0)+1
        if dick==dick2:
            return True
        else:
            return False

        