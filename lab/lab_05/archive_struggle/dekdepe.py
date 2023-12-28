grade_database = []  # List to store users' name and grades

# Action 1: Function to add the grades into the database
def add_the_grades():
    name = input("What's your name?: ").strip().lower()

    lab_grades = []  # List to store all the grades from a specific user name

    while True:  # Making sure to keep questioning until gets a valid value
        grade = input(
            f"Input your grade from Lab {len(lab_grades) + 1} (type STOP to finish): "
        )
        if grade.lower() == "stop":
            break

        grade = float(grade)  # Grade could be a float
        if 0 <= grade <= 100:  # Grade must be in range 0-100
            lab_grades.append(grade)  # Append to the database after validating it
        else:  # If the input is invalid
            print(
                "The grade should be in range 0-100. Please re-enter the grade."
            )

    grade_database.append({"name": name, "grades": lab_grades, "deleted_grades": []})  # Collect the data into the main database
    print()
    print(
        f"Successfully added {name}'s {len(lab_grades)} lab grades to the database."
    )

# Action 2: Function to display specific grade from the database
def display_the_grades():
    name = input("What's your name?: ").strip().lower()

    for student in grade_database:
        if student["name"] == name:
            lab_number = int(input("Enter the lab number to be displayed: "))
            if 1 <= lab_number <= len(student["grades"]):
                grade = student["grades"][lab_number - 1]
                print(f"The grade for Lab {lab_number} is {grade}")
            elif 1 <= lab_number <= len(student["deleted_grades"]):
                grade = student["deleted_grades"][lab_number - 1]
                print(f"The deleted grade for Lab {lab_number} is {grade}")
            else:
                print(f"No grade was found for Lab {lab_number}")
            return
    print("Name couldn't be found in the database.")

# Action 3: Update the existing grade in the database
def update_the_grades():
    name = input("What's your name?: ").strip().lower()

    for student in grade_database:
        if student["name"] == name:
            lab_number = int(input("Enter the lab number to be updated: "))
            if 1 <= lab_number <= len(student["grades"]):
                updated_grade = int(input("Enter the updated grade (0-100): "))
                if 0 <= updated_grade <= 100:
                    old_grade = student["grades"][lab_number - 1]
                    student["grades"][lab_number - 1] = updated_grade
                    print(
                        f"Successfully updated {name}'s Lab {lab_number} grade from {old_grade} to {updated_grade}."
                    )
                else:
                    print("The grade should be in the range 0-100. Please re-enter the grade.")
            else:
                print(f"No grade was found for Lab {lab_number}")
            return
    print("Name couldn't be found in the database.")

# Action 4: Function to delete a grade from the database
def delete_the_grades():
    name = input("What's your name?: ").strip().lower()

    for student in grade_database:
        if student["name"] == name:
            lab_number = int(input("Enter the lab number to be deleted: "))
            if 1 <= lab_number <= len(student["grades"]):
                deleted_grade = student["grades"].pop(lab_number - 1)
                student["deleted_grades"].append(deleted_grade)
                print(f"Successfully deleted {name}'s Lab {lab_number} grade from the database.")
            else:
                print("The grade should be in the range 0-100. Please re-enter the grade.")
            return
    print("Name couldn't be found in the database.")

# Functions for the main program
def main():
    while True:
        print()
        print("Welcome to the Dek Depe's Grade Database!")
        print("1. Add your grades to the database")
        print("2. View your grades from the database")
        print("3. Update you grades at the database")
        print("4. Delete your grades from the database")
        print("5. Exit the program")
    
        action = int(input("Choose your action (1--5): "))
        print()

        if action == 1:
            add_the_grades()
        elif action == 2:
            display_the_grades()
        elif action == 3:
            update_the_grades()
        elif action == 4:
            delete_the_grades()
        elif action == 5:
            print("Thank you for using Dek Depe's Grade Database")
            break
        
if __name__ == "__main__":
    main()
