import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales"],
    "Salary": [50000, 40000, 60000, 45000, 42000, 55000]
}

df = pd.DataFrame(data)

# Filter salaries greater than 45000
filtered = df[df["Salary"] > 45000]

print("Filtered Data:")
print(filtered)

# Group by department and calculate average salary
avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department:")
print(avg_salary)

# Plot Bar Chart
avg_salary.plot(kind="bar", color="skyblue")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()
