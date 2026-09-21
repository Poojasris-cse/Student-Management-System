students = []

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add Student
    if choice == 1:

        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        marks = float(input("Enter marks: "))

        students.append([student_id, name, age, marks])

        print("Student added successfully!")

    # View Students
    elif choice == 2:

        if len(students) == 0:
            print("No students found")
        else:
            print("\n===== STUDENT LIST =====")

            for student in students:

                if student[3] >= 90:
                    grade = "A+"
                elif student[3] >= 80:
                    grade = "A"
                elif student[3] >= 70:
                    grade = "B"
                elif student[3] >= 60:
                    grade = "C"
                elif student[3] >= 50:
                    grade = "D"
                else:
                    grade = "F"

                print(
                    "ID:", student[0],
                    "| Name:", student[1],
                    "| Age:", student[2],
                    "| Marks:", student[3],
                    "| Grade:", grade
                )

    # Search Student
    elif choice == 3:

        student_id = input("Enter student ID to search: ")
        found = False

        for student in students:

            if student[0] == student_id:

                print("\nStudent found!")
                print("ID:", student[0])
                print("Name:", student[1])
                print("Age:", student[2])
                print("Marks:", student[3])

                found = True
                break

        if not found:
            print("Student not found")

    # Update Student
    elif choice == 4:

        student_id = input("Enter student ID to update: ")
        found = False

        for student in students:

            if student[0] == student_id:

                student[1] = input("Enter new name: ")
                student[2] = int(input("Enter new age: "))
                student[3] = float(input("Enter new marks: "))

                print("Student updated successfully!")

                found = True
                break

        if not found:
            print("Student not found")

    # Delete Student
    elif choice == 5:

        student_id = input("Enter student ID to delete: ")
        found = False

        for student in students:

            if student[0] == student_id:

                students.remove(student)

                print("Student deleted successfully!")

                found = True
                break

        if not found:
            print("Student not found")

    # Exit
    elif choice == 6:

        print("Thank you for using Student Management System!")
        break

    else:

        print("Invalid choice! Please try again.")
