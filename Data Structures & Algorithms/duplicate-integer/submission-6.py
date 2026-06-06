class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_val=set()
        for i in nums:
            if i in check_val:
                return True
            else:
                check_val.add(i)
        return False
        