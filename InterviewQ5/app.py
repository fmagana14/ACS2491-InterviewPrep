
# Code
# Testcase
# Test Result
# Test Result
# 2937. Make Three Strings Equal
# Easy
# Topics
# Companies
# Hint
# You are given three strings: s1, s2, and s3. In one operation you can choose one of these strings and delete its rightmost character. Note that you cannot completely empty a string.

# Return the minimum number of operations required to make the strings equal. If it is impossible to make them equal, return -1.

 

# Example 1:

# Input: s1 = "abc", s2 = "abb", s3 = "ab"

# Output: 2

# Explanation: Deleting the rightmost character from both s1 and s2 will result in three equal strings.

# Example 2:

# Input: s1 = "dac", s2 = "bac", s3 = "cac"

# Output: -1

# Explanation: Since the first letters of s1 and s2 differ, they cannot be made equal.

 

# Constraints:

# 1 <= s1.length, s2.length, s3.length <= 100
# s1, s2 and s3 consist only of lowercase English letters.


class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
                lengths = [len(s1), len(s2), len(s3)]
                minimum_length = min(lengths)
                count = 0
                for i in range(minimum_length):
                    if s1[i] == s2[i] == s3[i]:
                        count += 1
                    else:
                        break
                if count == 0:
                    return -1
                result = sum(length - count for length in lengths)
                return result
    

    # Approach
# The algorithm calculates the length of the common prefix among the three strings. It then calculates the minimum length among the three strings and iterates through the common prefix. For each character in the common prefix, it checks if the corresponding characters in all three strings are equal. If they are, it increments a counter. The algorithm then calculates the result by subtracting the count from the total length of each string.

# Complexity
# Time complexity: O(min(n1, n2, n3)), where n1, n2, and n3 are the lengths of the three strings.
# Space complexity: O(1)