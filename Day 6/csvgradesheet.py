import csv

with open("marks.csv", "r") as infile, \
     open("results.csv", "w", newline="") as outfile:

    reader = csv.DictReader(infile)

    fieldnames = ["Name", "Math", "Science", "English", "Average"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:
        avg = (
            int(row["Math"]) +
            int(row["Science"]) +
            int(row["English"])
        ) / 3

        row["Average"] = round(avg, 2)
        writer.writerow(row)

print("Results written to results.csv")
