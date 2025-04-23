# Assignment: A0201 Stem-and-Leaf hw
# Name: Thuy Nguyen
# Date: Tuesday, April 15th, 2025
# Honor statement: I have not given or received any unauthorized assistance on this assignment.
# YouTube link: https://www.loom.com/share/cc2aab420fcd426197899f84245405ac?sid=3ecdc6ca-f023-45ad-94e9-555c7de7f062


def main():
    '''
    Ask the user to select dataset, read the data and display the stem-and-leaf plot.
    If user pass or enter any other value, the loop will exit.
'''
    while True:
        data = getData()
        if data is None: # exit if none of the suggested dataset is selected
            break
        stemAndLeaf(data) 


def getData():
    '''
    Ask the user for dataset number (1, 2 or 3) then read the corresponding dataset,
    finally return the dataset by the end of this function.
    Return None if user chooses to exit.
'''
    
    # ask user for a number from 1 to 3 to open an existing dataset 
    num = input('Please pick 1, 2 or 3 for dataset (pick 0 or another key to exit): ')
    if num not in ['1', '2', '3']:
        return None # exit condition

    filename = 'StemAndLeaf' + num + '.txt' # adjust the filename to StemAndLeafnum.txt
    infile = open(filename, "r") 
    lineList = infile.readlines()
    infile.close()

    # Make a list that includes all the numbers in the dataset
    numList = []

    # Use for loop to make sure it runs to the end of the dataset
    for i in range ( 0, len(lineList) ):
        x = int(lineList[i].strip())
        numList.append(x)
    return numList

def stemAndLeaf(d):
    '''
    Process to collect stems and their leaf/leaves.
    Use f" for better visualisation of stem-and-leaf display.
'''
    # Create a set to add all the 
    stems = {}
    
    for num in d:
        stem = num // 10
        leaf = num % 10
        
        if stem not in stems:
            stems[stem] = []
        
        stems[stem].append(leaf)
    for stem in stems:
        leaves = stems[stem]
        # print the stems and their leaf/leaves on seperate lines
        print(f"{stem}|{' '.join(str(leaf) for leaf in leaves)}")
    
