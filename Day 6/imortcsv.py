mport csv

# Writing data
students = [
    ["Name", "Marks"],
    ["Aman", 85],
    ["Priya", 92],
    ["Rahul", 78]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

# Reading data
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    print("Student Data:")
    for row in reader:
        print(row)
