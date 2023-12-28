grade_database = []                                                             # List to store users' name and grades

# Action 1: Function to add the grades into the database
def add_the_grades():
    name_input = input("What's your name?: ")
    name = name_input.strip().lower()

    for element in grade_database:                                              # Making sure user only can input the self-same name once
        if element[0] == name:
            print(
                "The name is already in the database.\n"
                "Redirecting to the main program..."
                )
            return

    lab_grades = []                                                             # List to store all the grades from a specific user name
                                                    
    while True:                                                                 # Making sure to keep questioning until gets a valid value
        grade = input(
            f"Input your grade from Lab {len(lab_grades) + 1} "\
             "(write STOP to finish): "
            )
        if grade.lower() == "stop":     
            break
            
        grade = float(grade)                                                    # Grade could be a float
        if 0 <= grade <= 100:                                                   # Grade must be in range 0--100
            lab_grades.append(grade)                                            # Append to the database after validating it
        
        else:                                                                   # If the input is invalid
            print(
                "The grade should be in range 0--100. "\
                "Please re-enter the grade."
                )
    
    grade_database.append([name, lab_grades])                                   # Collect the data into the main database      
    print()
    print(
        f"Successfully added {name_input}'s {len(lab_grades)} "\
        "lab grades to the database."
    )

# Action 2: Function to display user's specific lab grade
def display_the_grades():
    while True:
        name_input = input("What's your name?: ")
        name = name_input.strip().lower()

        for element in grade_database:
            if element[0].lower() == name:                                      # Make sure process only the existed name in the database
                lab_number = int(
                    input("Enter the lab number to be displayed: ")
                    )

                if 1 <= lab_number <= len(element[1]):                          # Lab number should be the existed number in the database
                    grade = element[1][lab_number - 1]                          # Access the specific grade from a specific lab

                    if grade is not None:                
                        print(
                            f"The grade for {name_input}'s Lab {lab_number} is {grade}"
                            )
                        return
                    else:                                                       # Handle case when user deleted a specific grade
                        print(
                            f"No grade was found for Lab {lab_number}"
                            )
                        return
                
                else:                                       
                    print(
                        f"No grade was found for Lab {lab_number}\n"
                        "Redirecting to the main program..."
                        )
                    return
        print(
            "Name couldn't be found in the database.\n"
            "Redirecting to the main program..."
            )    
        return  

# Action 3: Update the existing grade in the database
def update_the_grades():
    while True:
        name_input = input("What's your name?: ")
        name = name_input.strip().lower()

        for element in grade_database:
            if element[0].lower() == name:                                      # Make sure process only the existed name in the database
                lab_number = int(
                    input("Enter the lab number to be updated: ")
                    )

                if 1 <= lab_number <= len(element[1]):                          # Lab number should be the existed number in the database
                    updated_grade = int(
                        input("Enter the updated grade (0--100): ")
                        )
        
                    if 0 <= updated_grade <= 100:                               # Grade should be in range 0--100
                        old_grade = element[1][lab_number - 1]                  # Access the index of the grade that'd be processed
                        element[1][lab_number - 1] = updated_grade              # Replace the value at that index
                        print(
                        f"Successfully updated {name_input}'s Lab {lab_number} "\
                        f"grade from {old_grade} to {updated_grade}."
                        )
                        return
                    else:
                        print(
                        "The grade should be in range 0--100. "\
                        "Please re-enter the grade."
                        )
                else:
                    print(
                    f"No grade was found for Lab {lab_number}\n"
                    "Redirecting to the main program..."
                    )
                    return
            else:
                print(
                "Name couldn't be found in the database.\n"
                "Redirecting to the main program..."
                 )    
                return

# Action 4: Delete the existing grade in the database
def delete_the_grades():
    while True:
        name_input = input("What's your name?: ")
        name = name_input.strip().lower()

        for element in grade_database:
            if element[0].lower() == name:                              # Make sure process only the existed name in the database            
                lab_number = int(
                    input("Enter the lab number to be deleted: ")
                    )

                if 1 <= lab_number <= len(element[1]):                  # Lab number should be the existed number in the database
                    element[1][lab_number - 1] = None                   # Make sure the lab and grades won't shifted
                    print(
                        f"Successfully deleted {name_input}'s Lab {lab_number} "\
                        "grade from the database."
                        )
                    return
                else:
                    print(
                    "The grade should be in range 0--100. "\
                    "Please re-enter the grade."
                    )
            else:
                print("Name couldn't be found in the database.\n")
                print("Redirecting to the main program...")
                return

# Functions for the main program interface
def main():
    while True:                                    
        print()
        print("Welcome to the Dek Depe's Grade Database!")
        print("1. Add your grades to the database")
        print("2. View your grades from the database")
        print("3. Update you grades at the database")
        print("4. Delete your grades from the database")
        print("5. Exit the program")
        
        # User choose the specific action
        action = int(input("Choose your action (1--5): "))
        print()
        
        # Call the function based on the action choosen
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