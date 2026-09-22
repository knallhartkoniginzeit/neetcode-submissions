class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lis=set()
        for i in nums:
            if i not in lis:
                lis.add(i)
            else:
                return True
        return False        

