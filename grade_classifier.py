score = int(input("Enter your score (0-100): "))

# Check whether the score is outside the valid range.
if score < 0 or score > 100:
    print("Error: Score must be between 0 and 100.")
else:
    # Check whether the score is 80 or higher.
    if score >= 80:
        grade = "A"

    # Check whether the score is between 70 and 79.
    elif score >= 70:
        grade = "B"

    # Check whether the score is between 60 and 69.
    elif score >= 60:
        grade = "C"

    # Check whether the score is between 50 and 59.
    elif score >= 50:
        grade = "D"

    # Any valid score below 50 gets F.
    else:
        grade = "F"

    print(f"A score of {score} earns grade: {grade}")
