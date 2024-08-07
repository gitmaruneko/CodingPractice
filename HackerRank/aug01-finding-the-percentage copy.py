#!/bin/python3

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika


if __name__ == '__main__':

    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input() 

#solution 1
    query_score = student_marks.get(query_name)
    total = sum(query_score)
    print("%.2f"%(total/len(query_score)))


# solution opt


    
