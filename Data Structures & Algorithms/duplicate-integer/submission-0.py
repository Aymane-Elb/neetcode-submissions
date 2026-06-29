class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers={}
        for i in nums:
            if i in numbers:
                numbers[i]+= 1
                if numbers[i]>1:
                    return True
            else:
                numbers[i]=1
                
        return False