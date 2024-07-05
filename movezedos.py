'''
Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sam = 0
        jenna = 0
        while True:
            for sam in range(sam, 1+len(nums)):
                if sam == len(nums):
                    return
                if nums[sam] == 0:
                    break
            for jenna in range(max(sam, jenna), 1+len(nums)):
                if jenna == len(nums):
                    return
                if nums[jenna] != 0:
                    break
            tmp = nums[jenna]
            nums[jenna] = nums[sam]
            nums[sam] = tmp


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    # [4,3,2,1]
    nums=[0, 1, 0, 3, 0 ,0,0,0,0]
    answer = sol.moveZeroes(nums)
    print(nums)
