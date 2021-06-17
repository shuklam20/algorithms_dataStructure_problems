'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        out = []
        mapping1 = {'(':')', '{':'}', '[':']'}
        mapping2 = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in mapping1.keys():
                out.append(i)
            else:
                if len(out) == 0:
                    return False 
                if (i in mapping2.keys() and out[-1] == mapping2[i]):
                    out.pop()
                else:
                    return False
        return len(out)==0
                