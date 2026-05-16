import json

# ------ Step 1: Load data in students.json file ------
try: 
    with open ("students.json", "r") as file:
        student_data = json.load(file)
except FileNotFoundError:
    student_data = []

# ------ Step 2: Create a function to save data ------
def save_data():
    with open ("students.json", "w") as file:
        json.dump(student_data, file, indent=4)

# ------ Step 3: Create a new student ------
def create():
    name = input("Name: ")
    grade = input("Class: ")

    student = {
        "id" : len(student_data) + 1,
        "name" : name,
        "class" : grade
    }
    student_data.append(student)
    save_data()

# ------ Step 4: Show all student ------
def read():
    for student in student_data:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Class: {student['class']}")
        print("-" * 45)

# ------ Step 5: Change student data ------
def update():
    read()

    update_id = int(input("Enter the student ID you want to change: "))
    new_name = input("Enter a new name: ")
    new_class = input("Enter a new class: ")
    found = False

    for student in student_data:
        if student['id'] == update_id:
            student["name"] = new_name
            student["class"] = new_class
            found = True
            print("--- Data updated successfully ---")
            save_data()
    if not found:
        print("--- Data invalid ---")

# ------ Step 6: Delete student data ------
def delete():
    read()

    remove_id = int(input("Enter the student ID you want to delete: "))
    found = False

    for student in student_data:
        if student['id'] == remove_id:
            student_data.remove(student)
            found = True
            print("--- Student deleted ---")
            save_data()
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