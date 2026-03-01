data = """student , grade
michael , 67
SARA , 94
james , 81
LUNA , 73
oscar , 89
"""
Top = 0
Top_Student = ""
rows = data.split("\n")
for row in rows:
    if "student" in row:
        continue
    if row == "":
        continue
    fields = row.split(",")
    name = fields[0].strip()
    grade = fields[1].strip()
    name = name.title()
    print(f"{name} - {grade}")
    grade = int(grade)
    if Top<grade:
        Top = grade
        Top_Student = name
print(f"Top student is: {Top_Student} - {Top}")
