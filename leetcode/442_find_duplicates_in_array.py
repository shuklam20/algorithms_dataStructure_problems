'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
#         # Method 1: 
#         ans = dict.fromkeys(list(range(1,len(nums) + 1)), 0)
#         ans_list = []
#         for i in nums:
#             ans[i] += 1
#         for k, v in ans.items():
#             if v == 2:
#                 ans_list.append(k)
                
#         return ans_list
    
        # Method 2: Negate the value at the position number defined by the number we are looking at, if the value has been seen, we will know since it will be negative.
        ans_list = []
        for i in nums:
            if nums[abs(i) - 1] < 0:
                ans_list.append(abs(i))
            else:
                nums[abs(i) - 1] *= -1 

        return ans_list
    