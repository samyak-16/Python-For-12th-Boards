import mysql.connector

# MySQL Connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="student_result"
)

cursor = con.cursor()

# Grade Calculation Function
def calculate_grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    else:
        return "F"

# Add Student Record
def addStudent():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Student Name: ")

    print("\nEnter Marks for the following subjects:")
    eng = int(input("English: "))
    phy = int(input("Physics: "))
    chem = int(input("Chemistry: "))
    math = int(input("Maths: "))
    comp = int(input("Computer Science: "))

    total = eng + phy + chem + math + comp
    percent = total / 5
    grade = calculate_grade(percent)

    query = "INSERT INTO result VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (roll, name, eng, phy, chem, math, comp, total, percent, grade)

    cursor.execute(query, data)
    con.commit()
    print("\n✔ Student Record Added Successfully!\n")

# Display All Students
def displayAll():
    cursor.execute("SELECT * FROM result")
    rows = cursor.fetchall()

    if not rows:
        print("\nNo records found.\n")
        return

    print("\n-------------------- STUDENT RESULT TABLE --------------------")
    print("ROLL | NAME        | ENG | PHY | CHEM | MATH | COMP | TOTAL | PERCENT | GRADE")
    print("--------------------------------------------------------------------------")

    for r in rows:
        print(f"{r[0]:<4} | {r[1]:<10} | {r[2]:<3} | {r[3]:<3} | {r[4]:<4} | {r[5]:<4} | {r[6]:<4} | {r[7]:<5} | {r[8]:<7.2f} | {r[9]}")
    
    print("--------------------------------------------------------------------------\n")


# Search Student by Roll No.
def searchStudent():
    roll = int(input("Enter Roll No to Search: "))
    query = "SELECT * FROM result WHERE roll = %s"
    cursor.execute(query, (roll,))
    r = cursor.fetchone()

    if r:
        print("\n-------------------- STUDENT RESULT --------------------")
        print("ROLL | NAME        | ENG | PHY | CHEM | MATH | COMP | TOTAL | PERCENT | GRADE")
        print("--------------------------------------------------------------------------")
        print(f"{r[0]:<4} | {r[1]:<10} | {r[2]:<3} | {r[3]:<3} | {r[4]:<4} | {r[5]:<4} | {r[6]:<4} | {r[7]:<5} | {r[8]:<7.2f} | {r[9]}")
        print("--------------------------------------------------------------------------\n")
    else:
        print("\n❌ No Record Found!\n")


# Update Marks for 5 Subjects
def updateMarks():
    roll = int(input("Enter Roll No to Update: "))

    print("\nEnter New Marks for the following subjects:")
    eng = int(input("English: "))
    phy = int(input("Physics: "))
    chem = int(input("Chemistry: "))
    math = int(input("Maths: "))
    comp = int(input("Computer Science: "))

    total = eng + phy + chem + math + comp
    percent = total / 5
    grade = calculate_grade(percent)

    query = """
        UPDATE result SET 
        eng=%s, phy=%s, chem=%s, math=%s, comp=%s,
        total=%s, percent=%s, grade=%s
        WHERE roll=%s
    """

    data = (eng, phy, chem, math, comp, total, percent, grade, roll)

    cursor.execute(query, data)
    con.commit()
    print("\n✔ Marks Updated Successfully!\n")

# Delete Record
def deleteStudent():
    roll = int(input("Enter Roll No to Delete: "))
    query = "DELETE FROM result WHERE roll=%s"

    cursor.execute(query, (roll,))
    con.commit()
    print("\n✔ Record Deleted Successfully!\n")

# Main Menu
while True:
    print("===== STUDENT RESULT MANAGEMENT SYSTEM (5 Subjects) =====")
    print("1. Add Student Result")
    print("2. Display All Results")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student Record")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        addStudent()
    elif choice == 2:
        displayAll()
    elif choice == 3:
        searchStudent()
    elif choice == 4:
        updateMarks()
    elif choice == 5:
        deleteStudent()
    elif choice == 6:
        print("Exiting Program…")
        break
    else:
        print("Invalid Choice! Try Again.\n")
