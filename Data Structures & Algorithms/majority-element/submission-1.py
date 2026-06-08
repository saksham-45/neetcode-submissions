class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=Counter(nums)
        print(s)
        maxv=0
        for i,v in s.items():
            if v>maxv:
                maxv=v
                maxi=i
        return maxi 


        