"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Difficulty: Easy
Pattern: hash set

Idea:
    A set drops duplicate entries. If the set is shorter than the list, at least one number appears more than once.

Time:  O(n) (34 ms)
Space: 13.7 MB

Notes:
    //
"""


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_a = set(nums)
        if len(set_a) == len(nums):
            return False
        return True
