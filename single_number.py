'''
how to solve this problem

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1


Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''
# you's too four loops
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i != j:
                    break
            else:
                return nums[i]


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    # [4,1,2,1,2], [1], [2, 2, 1]
    nums = [2, 2, 1]
    answer = sol.singleNumber(nums)
    print(answer)
