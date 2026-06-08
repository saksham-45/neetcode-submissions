import collections
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        ''' s=Counter(nums)
            k=0
            for idx ,(key,value) in enumerate(s.items()):
                if key!=val:
                    nums[idx]=key
            print(nums)'''
        
        
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
        
        
       


            
            