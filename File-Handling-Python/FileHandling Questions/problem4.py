# Write a program to:

# Create a binary file student.dat
# Store records of students (name and marks)

import pickle

n = int(input("Enter number of students :"))
records = []

for i in range(n):
    name = input(f"Enter name for student {i + 1}")
    marks = input(f"Enter marks for student {i + 1}")
    data = {"name": name, "marks": marks}
    records.append(data)

with open("student.dat", "wb") as f:
    pickle.dump(records, f)
