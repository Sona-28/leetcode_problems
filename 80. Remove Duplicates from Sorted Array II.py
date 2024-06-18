#Question: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        tmp = None
        i=1
        for x in range(1, len(nums)):
            if nums[x]!=tmp:
                if nums[x] == nums[x-1]:
                    tmp=nums[x]
                nums[i]=nums[x]
                i+=1
        return i