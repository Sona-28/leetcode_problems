# Question: https://leetcode.com/problems/rotate-array/description

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k!=0 and k%len(nums)!=0:
            k = k % len(nums)
            nums[:] = nums[-k:] + nums[:-k]