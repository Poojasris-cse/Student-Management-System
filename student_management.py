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

        name = input("Enter student name: ")
        age = int(input("Enter student age: "))

        students.append([name, age])

        print("Student added successfully!")

    # View Students
    elif choice == 2:

        if len(students) == 0:
            print("No students found")
        else:
            print("\nStudent List:")

            for student in students:
                print("Name:", student[0], "| Age:", student[1])

    # Search Student
    elif choice == 3:

        name = input("Enter student name to search: ")
        found = False

        for student in students:

            if student[0].lower() == name.lower():

                print("\nStudent found!")
                print("Name:", student[0])
                print("Age:", student[1])

                found = True
                break

        if not found:
            print("Student not found")

    # Update Student
    elif choice == 4:

        name = input("Enter student name to update: ")
        found = False

        for student in students:

            if student[0].lower() == name.lower():

                new_name = input("Enter new name: ")
                new_age = int(input("Enter new age: "))

                student[0] = new_name
                student[1] = new_age

                print("Student updated successfully!")

                found = True
                break

        if not found:
            print("Student not found")

    # Delete Student
    elif choice == 5:

        name = input("Enter student name to delete: ")
        found = False

        for student in students:

            if student[0].lower() == name.lower():

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
