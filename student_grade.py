import csv

def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

with open("marks.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["Name"]
        math = int(row["Math"])
        science = int(row["Science"])
        english = int(row["English"])
        avg = (math + science + english) / 3
        grade = get_grade(avg)

        with open(f"{name}_report.txt", "w") as report:
            report.write(f"Report Card - {name}\n")
            report.write(f"Math: {math}\n")
            report.write(f"Science: {science}\n")
            report.write(f"English: {english}\n")
            report.write(f"Average: {avg:.2f}\n")
            report.write(f"Grade: {grade}\n")

