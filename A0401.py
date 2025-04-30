# Assignment: A0401 Updated Goldbach's Conjecture hw
# Name: Thuy Nguyen
# Date: Tuesday, April 29th, 2025
# Honor statement: I have not given or received any unauthorized assistance on this assignment.
# YouTube link: https://www.loom.com/share/690b16c030734208b3fb77368d67c617?sid=1ac1aba4-5b1a-44fc-bd8b-c2ae5ab7c159


def main():
    """
    Call user_input() function firstly to get lst and target_sum variables.
    Then use binary search inside a loop to determine if there's two numbers add up to the target value.
    The time take to complete this program should be O(nlogn).   
"""
    
    lst, target_sum = user_input()
    print(f"Our sorted list is {lst} and the target sum is {target_sum}")
    
    for i in range(len(lst)):
        num = lst[i]
        val = target_sum - num
        low = 0 # Begin index
        high = len(lst) - 1 # End index
        
        # Reuse binary loop we used in class for this exercise
        while low <= high: 
            mid = (low + high)//2 # Middle index
            midval = lst[mid] # Middle index value
            if val == midval:
                print(f"Two numbers that make up the target sum are {num} and {val}.")
                return
            elif val < midval:
                high = mid - 1
            else:
                low = mid + 1
    print("No two numbers in the list add up to the target sum.")



def user_input():
    """
    Ask the user for an input of the list length to generate the random numbers list.
    List length needs to be from 2-100 because we're looking for 2 numbers that add up to a value.
    Return a sorted list of integers and the targeted sum.
"""
    import random 
    while True: 
        try:
            lstlen = int(input("Enter the desired list length between 2 and 100: "))
            if 2<= lstlen <=100:
                break
            else:
                print("List length must be between 2 and 100 because we're looking for 2 numbers that add up to a value.")
                
        except ValueError: 
            print("Invalid input. Enter an eligible integer!")

    
    lst = []
    for i in range(lstlen):
        lst.append(random.randint(0,100)) # Append lstlen random num in that range to lst
    lst.sort() # Sort list lst
    print(f"Our sorted list is {lst}")

    min_val = lst[0]
    
    while True: # Ask for target sum
        try:
            target_sum = int(input(f"Enter a target sum that is greater than {min_val}: "))
            if target_sum > min_val: # Break if req is satisfied
                break
            else:
                print(f"Target sum must be greater than the smallest value in the list.")


        except ValueError:
            print("Invalid input. Enter a valid integer!")


    return lst, target_sum

