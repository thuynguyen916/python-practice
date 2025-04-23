# Assignment: A0101 Grading Logic hw
# Name: Thuy Nguyen
# Date: Sunday, April 6th, 2025
# Honor statement: I have not given or received any unauthorized assistance on this assignment.
# YouTube link: https://www.loom.com/share/4fa5a504201442a195f8ef7d4be8816a?sid=b8e937d5-e937-43ce-8eb5-2f830d27ff71


def gradingLogic():
    
    """
Ask a series of 4 questions to see if the submission is qualified basic requirements.

Once met, function points will be used based on correctness, elegance, hygiene and Youtube discussion quality.
    
Points are in float data type.

If the work is submitted late, points will be deducted by 1% of total grade by each hour.

Final grade will be returned as a float.

"""

    grade = 0
    
    if not basicReqMet(): 
        return grade # Students will receive 0 if they don't pass basic requirements.
    else: 
        grade = points()

        if lateWork():
            # lateWork function is indented because it only needs to be considered if basic requirements are met. 
            timeLate = int(input('How many hours late is it? '))
            if timeLate < 100:
                grade = grade*(100-timeLate)/100
            else:
                grade = 0
        return grade

def basicReqMet():    
    
    """
Check for basic requirements: file format, student name, honor statement and video link included.

Automatically stop asking questions if one is disqualified (from top to bottom) using return T/F.
"""
    
    hasCorrectFile = int(input('Assignment submitted as a single uncompressed .py file; 0 = No, 1= Yes: '))
    if hasCorrectFile == 0:
        return False

    
    hasName = int(input('Submission includes the student''s name and date; 0 = No, 1= Yes: '))
    if hasName == 0:
        return False

    hasHonorStatement = int(input('Assignment includes the honor statement; 0 = No, 1= Yes: '))
    if hasHonorStatement == 0:
        return False

    hasVideo = int(input('Assignment includes a video presenting code;  0 = No, 1= Yes: '))
    if hasVideo == 0:
        return False

    return True # Return True if all basic requirements are met.

def points():
    """
Ask 4 questions to about correctness, elegance, hygiene and video on Youtube to get score.

Return score total.
"""
    correctnessPoints = float(input('Points for the correctness of the code: '))
    elegancePoints = float(input('Points for the code elegance: '))
    codeHygienePoints = float(input('Points for the code hygiene: '))
    qualityYTPoints = float(input('Points for the quality of the discussion on the Youtube video: '))

    return correctnessPoints + elegancePoints + codeHygienePoints + qualityYTPoints
    
def lateWork():
    """
Check if assignment is submitted late using return T/F.
"""
    isLate = int(input('Was the assignment submitted late?; 0 = No, 1 = Yes: '))
    if isLate == 1:
        return True
    return False
