students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        students.append([name, age])
        print("Student added successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No students found")
        else:
            for student in students:
                print("Name:", student[0], "Age:", student[1])

    elif choice == 3:
        name = input("Enter student name to search: ")
        found = False

        for student in students:
            if student[0].lower() == name.lower():
                print("Student found!")
                print("Name:", student[0])
                print("Age:", student[1])
                found = True
                break

        if not found:
            print("Student not found")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
