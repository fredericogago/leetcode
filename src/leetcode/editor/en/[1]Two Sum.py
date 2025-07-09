"""
Problem: Two Sum
LeetCode: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Tags: Array, HashMap
"""

# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target. 
# 
#  You may assume that each input would have exactly one solution, and you may 
# not use the same element twice. 
# 
#  You can return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [3,3], target = 6
# Output: [0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  Only one valid answer exists. 
#  
# 
#  
# Follow-up: Can you come up with an algorithm that is less than 
# O(n²)
#  time complexity?
# 
#  Related Topics Array Hash Table 👍 62334 👎 2260


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Find the indices of the two numbers in `nums` that add up to `target`.

        Uses a single-pass hash table approach to achieve O(n) time complexity.

        Args:
            nums (List[int]): A list of integers.
            target (int): The target sum to find.

        Returns:
            List[int]: A list containing the two indices whose values sum to `target`.

        Raises:
            ValueError: If no two numbers sum to the target (though by problem constraints, this won't occur).
        """
        complement_map: dict[int, int] = {}
        for index, num in enumerate(nums):
            # If current number matches a previously stored complement, return the pair of indices
            if num in complement_map:
                return [complement_map[num], index]
            # Otherwise, store the complement of the current number
            complement_map[target - num] = index
        # Under the problem constraints, this line should never be reached
        raise ValueError("No two sum solution")
# leetcode submit region end(Prohibit modification and deletion)
