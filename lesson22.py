# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.

def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1

#print factorial(0)
#>>> 1

#print factorial(5)
#>>> 120

#print factorial(10)
#>>> 3628800





# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    if len(s) == 0:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

#print is_palindrome('')
#>>> True
#print is_palindrome('abab')
#>>> False
#print is_palindrome('abba')
#>>> True





# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

#print fibonacci(0)
#>>> 0
#print fibonacci(1)
#>>> 1
#print fibonacci(15)
#>>> 610





#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

'''
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    h1 = 0
    h2 = 1
    c = 1
    while c < n:
        out = h1 + h2
        h1 = h2
        h2 = out
        c += 1
    return out
'''

def fibonacci(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current

#print fibonacci(36)
#>>> 14930352
