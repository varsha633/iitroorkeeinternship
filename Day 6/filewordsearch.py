filename = "data.txt"
keyword = input("Enter keyword to search: ")

found = False

with open(filename, "r") as file:
    for line_no, line in enumerate(file, start=1):
        if keyword.lower() in line.lower():
            print(f"Line {line_no}: {line.strip()}")
            found = True

if not found:
    print("Keyword not found.")
