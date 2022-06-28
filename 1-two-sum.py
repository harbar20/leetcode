"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        def twoSumHelper(nums, i1, i2, target):
            num1 = nums[i1]
            num2 = nums[i2]
            test = num1 + num2

            if test == target:
                return [num1, num2]
            elif test > target:
                return twoSumHelper(nums, i1, i2 - 1, target) # move right hand inwards, decreasing test
            else:
                return twoSumHelper(nums, i1 + 1, i2, target) # move left hand inwards, increasing test
        
        sortedNums = sorted(nums)
        sortedIndexNums = twoSumHelper(sortedNums, 0, len(sortedNums)-1, target)
        numsCopy = nums
        
        num1 = sortedIndexNums[0]
        num2 = sortedIndexNums[1]
        
        index1 = numsCopy.index(num1)   
        if num1 == num2:
            numsCopy.remove(num1)
            index2 = numsCopy.index(num2) + 1
        else:
            index2 = numsCopy.index(num2)
        
        return [index1, index2]