'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1
 

Constraints:

2 <= n <= 3 * 104
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times

'''

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        Sol 1: O(nlog(n)) through sorting
        '''
#         nums.sort()
#         for i in range(len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 return nums[i]
            
        '''
        Sol 2: O(n) time and space complexity using set
        '''
        # ans = set()
        # for i in nums:
        #     if i in ans:
        #         return i
        #     ans.add(i)
            
        '''
        Sol 3: O(n) time complexity using LinkedList, O(1) space
        '''        
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                fast = 0
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow
        