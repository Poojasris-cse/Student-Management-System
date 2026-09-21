students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        students.append([name, age])
        print("Student added successfully!")

    elif choice == 2:
        for student in students:
            print("Name:", student[0], "Age:", student[1])

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
