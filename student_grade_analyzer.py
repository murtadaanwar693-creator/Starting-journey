students = [
    {"name": "Alice",   "scores": [85, 90, 78, 92, 88], "attendance": 95},
    {"name": "Bob",     "scores": [40, 55, 60, 45, 50], "attendance": 61},
    {"name": "Charlie", "scores": [70, 68, 74, 80, 65], "attendance": 78},
    {"name": "Diana",   "scores": [95, 98, 100, 92, 97], "attendance": 99},
    {"name": "Eve",     "scores": [30, 40, 25, 50, 35], "attendance": 45},
]
total = 0
grade = ''
status = ""
for i in range (len(students)):
    for row in students [i] ["scores"]:
        total += float(row)
    average = total / len(students [i] ["scores"])
    total = 0
    attendance = students [i] ["attendance"]
    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >=50:
        grade = 'D'
    elif average <50:
        grade = 'F'
    else:
        print("Incorrect average!")
    if attendance >= 65 and (grade == 'A' or grade == 'B' or grade == 'C'):
        status = "Good Standing!"
    else:
        status = "At Risk!"
    print(f"{students [i] ["name"]}   | Avg = {average} | Grade: {grade} | Status: {status} ")