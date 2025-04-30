# Assignment: A0402 Human Pyramid hw
# Name: Thuy Nguyen
# Date: Tuesday, April 29th, 2025
# Honor statement: I have not given or received any unauthorized assistance on this assignment.
# YouTube link: https://www.loom.com/share/15203e7e88c7481d996b09b727358a7f?sid=8d2b00a1-0f46-45b2-9786-78a8f6aac244

def humanPyramid(row, column):
    """
    Calculate and return the weight of the person who're standing in the index provided.
    Each person weights 128lbs and the person right below them carries half of their weights,
    plus whatever they're carrying.
    Parameters: row and column, which are index of the person.
"""
    if row == column == 0: # Person on top of the pyramid
        return  0
    
    elif column == 0: # People who're on the left edge of the pyramid
        # The person that gives direct weight and the weight they're carrying from above.
        return 0.5*(128+ humanPyramid((row-1), column))

    elif column == row: # People who're on the right edge of the pyramid
        # The person that gives direct weight and the weight they're carrying from above.
        return 0.5*(128+ humanPyramid((row-1), (column-1)))
    
    else: # Everyone else inside the pyramid who carries the weight of two people above them.
        return 0.5*(128+ humanPyramid((row-1),(column-1)))+ 0.5*(128+ humanPyramid((row-1), column))
