"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Difficulty: Easy
Pattern: brute force (nested loops)

Idea:
    Check every pair of numbers once. The inner loop starts at `i + 1`, so no pair is tested twice and no element is paired with itself.

Time:  O(n2)
Space: O(1)

Notes:

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l):
            for j in range(i + 1, l, 1):
                if nums[i] + nums[j] == target:
                    return [i, j]
