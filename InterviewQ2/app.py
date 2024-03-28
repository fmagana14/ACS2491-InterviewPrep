# 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

# INITIAL ATTEMPT

# class Solution:
#     def searchInsert(nums: List[int], target: int) -> int:
#         l = 0 
#         r = len(nums) - 1
#         while l <= r:
#             mid = (l+r)//2
#             if nums[mid] < target:
#                 l = mid + 1
#             elif nums[mid] > target:
#                 r = mid - 1
#             else:
#                 return mid
#             return l
# 
# error recieved showed I didnt get displays of last two examples, got to rewrite 
# array in order to reach an output of 4 and 1.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            mid=(l+r)//2
            if nums[mid]>=target:
                r=mid-1
            else:
                l=mid+1
        return r+1
# took elif array out due to it returning r instread of L at the midpoint,
    # with these changes it should only return r after the loop is completed.