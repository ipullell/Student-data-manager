import json

data_student = []

# ------ Step 1 : Create a new student ------
def create():
    name = input("Name: ")
    grade = input("Class: ")

    student = {
        "id" : len(data_student) + 1,
        "name" : name,
        "class" : grade
    }
    data_student.append(student)

# ------ Step 2: Show all student ------
def read():
    for student in data_student:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Class: {student['class']}")
        print("-" * 45)

# ------ Step 3: Change student data ------
def update():
    for x in data_student:
        print(f"ID: {x['id']}")
        print(f"Name: {x['name']}")
        print(f"Class: {x['class']}")
        print("-" * 45)

    update_id = int(input("Enter the student ID you want to change: "))
    new_name = input("Enter a new name: ")
    new_class = input("Enter a new class: ")
    found = False

    for student in data_student:
        if student['id'] == update_id:
            student["name"] = new_name
            student["class"] = new_class
            found = True
            print("--- Data updated successfully ---")
    
    if not found:
        print("--- Data invalid ---")

# ------ Step 4: Delete student data ------
def delete():
    for x in data_student:
        print(f"ID: {x['id']}")
        print(f"Name: {x['name']}")
        print(f"Class: {x['class']}")
        print("-" * 45)

    remove_id = int(input("Enter the student ID you want to delete: "))
    found = False

    for student in data_student:
        if student['id'] == remove_id:
            data_student.remove(student)
            found = True
            print("--- Student deleted ---")

    if not found:
        print("--- Sorry, the ID you entered is invalid ---")


# ------ Menu program Data list ------
while True:
    print("\n\n--- Welcome in my mini project Data List manager ---")
    print("1. Create a new data")
    print("2. Read student data")
    print("3. Change a student data")
    print("4. Delete student data")
    print("5. Exit a program\n")

# ------ Handle error ------
    try:
        choice = int(input("Enter options: "))
        print( )
    except ValueError:
        print("Sorry, your choice is not available in our program")
        continue

# ------ Input Menu user ------
    if choice == 1:
        create()
    elif choice == 2:
        read()
    elif choice == 3:
        update()
    elif choice == 4:
        delete()
    elif choice == 5:
        break

# ------ Save to json file ------
    pass