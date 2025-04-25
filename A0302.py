# Assignment: A0302 Happy Number hw
# Name: Thuy Nguyen
# Date: Monday, April 21st, 2025
# Honor statement: I have not given or received any unauthorized assistance on this assignment.
# YouTube link: https://www.loom.com/share/d8021c528fcf4e6b812338a310571073?sid=94320e12-4bb4-4d2a-9389-47031d68f885



def main(): 

    """
    Use a while loop to verify if the number is a positive integer.
    The loop should run endlessly unless get a finish flag.
    Print the sequence of the number that help determine if it's a Happy number.
    Finally, summarize all the numbers in a dictionary.

    """
    ans = {}
    happystatus = {True: "happy", False: "sad"}
    
    while True:
        num = input("Enter a positive number, or enter nothing to pass: ")
        # "" is chosen as a flag to finish
        if num == "": 
            break

        try:
            intnum = int(num)
            if intnum <= 0: # Needs to be a positive integer
                print("Need to be a positive number.")
                continue
            
            # Assign to variables so that function isHappy(n) will not be called twice
            is_happy, lst = isHappy(intnum)
            
            print(f"{intnum} is a {happystatus[is_happy]} number: {lst}")

            ans[intnum] = (happystatus[is_happy], lst) # Add number, its happy status and its sequence to the ans dictionary

        except ValueError: # Catch ValueError using try-except
            print("Invalid input. Please enter a valid integer.")
            
    print()        
    print("Summing up the results:")
    print(ans)

def isHappy(n):
    """
    Check if the given number is a happy number.
    Stop when the updated numberis 1 or already in the sequence n_lst.
    Parameter:
    n(int) is the number to check
    Return:
    (bool,n_lst): Tuple used when called by main() function.
    """
    n_lst = [] # Sequence of numbers to eventually find out if n is a happy number
    
    while n!= 1 and n not in n_lst: # Condition to stop if num in sequence is sad
        n_lst.append(n)
        
        ds = list(int(d) for d in str(n)) # Create a list of digits in number n
        
        n = sum(d**2 for d in ds) # New n= total of all squared digits from old n
        
    n_lst.append(n) # The last value, which is either 1 or a number that is already in lst

    if n_lst[-1] == 1: 
        return True, n_lst # If the last number is 1, it's a happy number
    else:
        return False, n_lst ## If the last number is not 1, it's not a happy number
