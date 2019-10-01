# """
# LeetCode problem 49: Group Together Anagrams
# We use a dictionary (i.e. HashMap) to check for anagrams
# Time Complexity: O(nk)
# """
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        result = []
        for word in strs:  # O(n) words
            # freeze set to use dictionary as key, keys are immutable in python
            key = frozenset(self.buildMap(word).items())  # O(k), where k is the maximal length of word
            if key in group:
                group[key].append(word)  # O(1)
            else:
                group[key] = [word]  # O(1)
        for list in group.values():
            result.append(list)  # O(n), only called once
        return result

    def buildMap(self, word):
        d = {}
        for letter in word:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
        return d


# basic tests
sol = Solution()
print(sol.groupAnagrams(["abc", "bca", "aaa", "bbb", "cba"]))
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
