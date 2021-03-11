"""Implement a function recursively to get the desired
Fibonacci sequence value."""

def get_fib(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fib(position - 1) + get_fib(position - 2)

def get_fib_dict(position):
    ans = {0:0, 1:1}
    for i in range(2, position+1):
        ans[i] = ans[i-1] + ans[i-2]
    return ans[position]

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)

# Using dictionary to store the values
print get_fib_dict(9)
print get_fib_dict(11)
print get_fib_dict(0)