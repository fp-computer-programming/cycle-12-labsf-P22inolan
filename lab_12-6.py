# Author: IBN (AMDG) 3/1/2022
grades = {100: "end_s1_labs", 100: "end_s2_labs", 0: "cycle_10_labs", 100: "mid_year_project_proposal", 100: "cycle_10_practice_quiz", 80: "cycle_10_quiz"}
print(grades.keys())

for (k, v) in grades.items():
    print(k, v)

for (k, v) in grades.items():
    if k > 70:
        print(k, v)

for (k, v) in grades.items():
    if k < 50:
        print(k, v)
