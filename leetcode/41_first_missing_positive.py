'''
Given an unsorted integer array nums, find the smallest missing positive integer.
 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1

'''


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If an empty list is given
        if len(nums) == 0:
            return 1
        
        # first missing value is correlated with the range of input array length
        ans = dict.fromkeys(list(range(1, len(nums) + 1)))
        
        for i in nums:
            if i <= 0 or i > len(nums):
                continue
            ans[i] = 0
            ans[i] += 1
            
        for k, v in ans.iteritems():
            if v is None:
                return k
            
        # default list is perfectly only of the type [1,2,3,.....]
        return len(nums) + 1
        
