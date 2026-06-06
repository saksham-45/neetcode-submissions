import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      res= defaultdict(list)
      for s in strs:
        idx=[0]*26
        for ch in s:
            chs= ord(ch)-ord('a')
            idx[chs]+=1
        res[tuple(idx)].append(s)
      return list(res.values())

      