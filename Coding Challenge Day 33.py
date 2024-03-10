#Write a test case for a function that checks if a number is prime

import pytest
num = 22
flag = 0

for i in range(2,num):
    if num % i == 0:
        flag = 1
    break
if flag == 0:
    print(f'{num} is a prime number.')
else:
    print(f'{num} is not a prime number.')


#Test code using PyTest
def test_always_passes():
    assert flag == 1

def test_always_fails():
    assert flag == 0

