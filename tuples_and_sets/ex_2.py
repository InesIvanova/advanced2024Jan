n = int(input())

student_grades = {}

for _ in range(n):
    name, grade_as_str = tuple(input().split())
    grade = float(grade_as_str)

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

for name, grades in student_grades.items():
    avg_grade = sum(grades) / len(grades)
    formatted_grades = f"{' '.join([f'{g:.2f}' for g in grades])}"
    print(f"{name} ->", *formatted_grades, f"(avg: {avg_grade:.2f})")