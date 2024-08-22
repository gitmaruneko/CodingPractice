#!/bin/python3

if __name__ == '__main__':

# 5 Harry 37.21 Berry 37.21 Tina 37.2 Akriti 41 Harsh 39
# 4 Rachel -50 Mawer -50 Sheen -50 Shaheen 51  

#solution 1
    student_total = []
    student_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_total.append([name, score])
        if score not in student_score:
            student_score.append(score)

    student_score.sort()
    second_lowest = student_score[1]
    name = []
    for student in student_total:
        if student[1] == second_lowest:
            name.append(student[0])
    
    name.sort()
    for item in name:
        print(item)

# solution opt

    # students = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
        
    #     students.append([name, score])
    
    # lowest = min([el[1] for el in students])
    # second_low = min(list(filter(lambda a: a > lowest, [el[1] for el in students])))
    
    # out = [el[0] for el in students if (el[1] == second_low)]
    # out.sort()
    
    # print("\n".join(out))
    
