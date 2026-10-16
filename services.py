from config import GRADE_A_THRESHOLD, GRADE_B_THRESHOLD, GRADE_C_THRESHOLD, GRADE_D_THRESHOLD

def calculate_grade(score):
    if score >= GRADE_A_THRESHOLD:
        return 'A'
    elif score >= GRADE_B_THRESHOLD:
        return 'B'
    elif score >= GRADE_C_THRESHOLD:
        return 'C'
    elif score >= GRADE_D_THRESHOLD:
        return 'D'
    else:
        return 'F'

def calculate_statistics(students):
    if not students:
        return {"total_students": 0, "average_score": 0.0, "highest_score": 0, "lowest_score": 0}
    
    scores = [student["Score"] for student in students]
    return {
        "total_students": len(scores),
        "average_score": round(sum(scores) / len(scores), 1),
        "highest_score": max(scores),
        "lowest_score": min(scores)
    }
