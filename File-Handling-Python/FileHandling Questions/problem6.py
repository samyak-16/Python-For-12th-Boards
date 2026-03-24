# # Write a program to:

# # Search for a student by name in student.dat
# # Display the record if found

# import pickle


# name = input("Enter name : ")
# with open("student.dat", "rb") as f:
#     records = pickle.load(f)
#     for record in records:
#         if record.get(name):
#             print(f"Name : {name}  Marks: {record[name]}")

#         else:
#             break
#     else:
#         print("No Record found")
