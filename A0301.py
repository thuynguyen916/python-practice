# Assignment: A0301 Goldbach's Conjecture hw
# Name: Thuy Nguyen
# Date: Sunday, April 20th, 2025
# Honor statement: I have not given or received any unauthorized assistance on this assignment.
# YouTube link: https://www.loom.com/share/9a3cd7b55bec4b4f95bf036951be143a?sid=1b7dfb59-de9b-49a1-a6ea-fa8053d82514

def main():
    '''
    Go through even numbers from 4 to 100 and
    find one pair of prime numbers that add up to each.

    For every even number, check pairs starting from 2 up to half the number.
    If both numbers in the pair are prime, print them. Only print 1 pair per each integer.
'''
    # Iterate over the itegers from 4 to 100, even numbers only
    for num in range(4,101,2):
        
        # Iterate from 2 because 1 is not a prime number
        # Max in range is num//2 +1 because b+a = a+b
        for i in range(2, num//2 +1): 
            rem = num - i # Rem stands for remainder

            # Check if the 2 numbers are both prime numbers
            if is_prime(i) is True and is_prime(rem) is True: 
                print(f"{num} = {i} + {rem}") # Format: int = primenum1 + primenum2
                break # Only show 1 pair of prime numbers for each integer
        

def is_prime(n):
    """
    Check if a given number is a prime number.

    A prime number is a number greater than 1 that has no positive divisors 
other than itself.

    Returns True if the number is prime, False otherwise.
    """
    
    if n <= 1: # 0, 1 are not prime numbers
        return False
    for i in range(2, int(n**0.5) +1): # Only need to iterate up to sqrt(n)
        if n%i == 0: # Check if the number is non-prime number
            return False
    return True
