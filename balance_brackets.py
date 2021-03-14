'''
From Facebook interview practice question:

A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
We consider two brackets to be matching if the first element is an open-bracket, e.g., (, {, or [, 
and the second bracket is a close-bracket of the same type, e.g., ( and ), [ and ], and { and } are 
the only pairs of matching brackets. Furthermore, a sequence of brackets is said to be balanced if 
the following conditions are met:
>> The sequence is empty, or
>> The sequence is composed of two, non-empty, sequences both of which are balanced, or
>> The first and last brackets of the sequence are matching, and the portion of the sequence without the first and last elements is balanced.
'''




def isBalanced(s):
  out = []
  for i in s:
    if (i=='[' or i=='{' or i=='('):
      out.append(i)
    else:
      if len(out) == 0:
        return False
      if ((i=='}' and out[-1]=='{') or (i==')' and out[-1]=='(') or (i==']' and out[-1]=='[')):
        out.pop()
      else:
        return False
  return len(out)==0


# Example 1 - output: true
s = "{[()]}"
print(isBalanced(s))


# Example 2 - output: true
s = "{}()"
print(isBalanced(s))

# Example 3 - output: false
s = "{(})"
print(isBalanced(s))

# Example 4 - output: false
s = ")"
print(isBalanced(s))