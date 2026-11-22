"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Difficulty: Easy
Pattern: sorting

Idea:
    if the sorted lists of characters ist equal, the words must be anagrams

Time:  O(n) 42ms
Space: 9.3 MB


Notes:
    //
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if sorted(s) != sorted(t):
            return False
        return True
