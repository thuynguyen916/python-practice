# Assignment: A0102 Coprime hw
# Name: Thuy Nguyen
# Date: Monday, April 7th, 2025
# Honor statement: I have not given or received any unauthorized assistance on this assignment.
# YouTube link: https://www.loom.com/share/92f08ce7f51d43698b33c145eee629fa?sid=31ae38ba-6bc2-4f4c-993d-f9f552c409ce


def coprime_test_loop():
    """
No matter if the numbers are coprime or not, if numbers are valid, the questions will be asked again.
"""
    while True:
        nums = get_nums()

        if not nums:
            print('These numbers are invalid!')
            break
        a, b = nums
        if coprime(a,b):
            print('These numbers are coprime.')
        else:
            print('These numbers are not coprime.')



def get_nums():
    """
Ask for 2 integer numbers a and b.
Return False if one of the numbers is invalid (in this case, is blank).
"""
    a= input('Enter the first number: ')
    if a != '':
        a= int(a)
        b= input('Enter the second number: ')
        if b != '':
            b=int(b)
            return a, b
        else:
            return False
    return False
            
    
def coprime(a,b):
    """
Check if the two numbers are co-prime.
"""
    if list(set(primeFac(a)) & set(primeFac(b))) == [1]:
        return True
    return False

def primeFac(num):
    """
Factorize the numbers that were given. Start with 1 because we'll iterate from range(2,...).
"""
    
    factors = [1] 
    for i in range(2, int(num**0.5) +1): 
        while num%i == 0:
            factors.append(int(i))
            num /=i
    if num>1: # This conditional statement is used for prime numbers
        factors.append(int(num))
    return factors
