#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fibonacci_last_digit(n):
    
    if (n <= 1):
        return n
    
    fib_1 = 0
    fib_2 = 1

    for i in range(n-1):
        fib_1, fib_2 = fib_2, (fib_1 + fib_2)%10
           
    return fib_2

n = int(input())
print(fibonacci_last_digit(n))

