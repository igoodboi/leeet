from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    # [4,3,2,1]
    answer = sol.containsDuplicate(nums= [1,1,1,3,3,4,3,2,4,2])
    print(answer)