#!/usr/bin/env python
# coding: utf-8

# 1.Write a Python program to check if the given number is a Disarium Number?

# In[6]:


def num_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count
def is_disarium_number(n):
    num_digits_n = num_digits(n)
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** num_digits_n
        num_digits_n -= 1
        temp //= 10
    if sum == n:
        return True
    else:
        return False
print(is_disarium_number(89))
print(is_disarium_number(98))
print(is_disarium_number(118))


# 2.Write a Python program to print all disarium numbers between 1 to 100?

# In[7]:


for i in range (1,101):
    if is_disarium_number(i):
        print(i)


# 3.Write a Python program to check if the given number is Happy Number?

# In[23]:


def sum_of_squares(n):
    sum = 0
    while n >0:
        digit =n % 10
        sum += digit ** 2
        n //= 10
    return sum
    
def is_happy_number(n):
    previous_sum = set()
    while n !=1:
        sum = sum_of_squares(n)
        if sum in previous_sum :
            return False
        previous_sum.add(sum)
        n = sum
    return True
print(is_happy_number(19))
print(is_happy_number(7))
print(is_happy_number(4))


# 4.Write a Python program to print all happy numbers between 1 and 100?

# In[24]:


for i in range(1, 101):
    if is_happy_number(i):
        print(i)


# 5.Write a Python program to determine whether the given number is a Harshad Number?

# In[28]:


def sum_of_digit(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10 
    return sum
def is_harshad_number(n):
    sum = sum_of_digit(n)
    if n % sum == 0:
        return True
    else:
        return False
    
print(is_harshad_number(79))
print(is_harshad_number(19))
print(is_harshad_number(9))


# 6.Write a Python program to print all pronic numbers between 1 and 100?

# In[30]:


for i in range (1 ,101):
    for j in range (1 ,i):
        if j *(j + 1) == i:
            print(i)
            break


# In[ ]:




