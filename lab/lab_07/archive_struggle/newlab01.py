# Store the family relations
def create_family_tree():
    return {}

# Check if the parent exists already in the dictionary
def add_relation(relations, parent, child):
    # Appends the child into the parent's list
    if parent in relations:
        relations[parent].append(child)
    # Otherwise, create a new entry for the parent and childs
    else:
        relations[parent] = [child]

# Check if a person is a descendant of another person recursively
def check_descendant(relations, parent, child):
    # Base case, if the parent nonexist in dict, the child isn't a descendant
    if parent not in relations:
        return False
    
    # Base case, If the child is directly listed as a child of the parent
    if child in relations[parent]:
        return True

    # Check if the child is a descendant of any children of the parent
    for descendant in relations[parent]:
        if check_descendant(relations, descendant, child):
            return True
    
    # The method doesn't find a match at a direct level and at a descendant level
    return False

# Display all descendants 
def print_descendants_helper(relations, person, generation):
    # Print with '-' tree indentation
    print(f"{'- ' * generation}{person}")
    
    # If there's information about the person given in the dictionary
    if person in relations:
        # Call itself recursively, child as the new person, increased generation
        for child in relations[person]:
            print_descendants_helper(relations, child, generation + 1)

def print_descendants(relations, parent):
    # If there's no information about the person given in the dictionary
    if parent not in relations:
        print(f"{parent} does not have any descendants.")
        return
    
    # Iterates through each child of the parent, recursively print their descendant
    for child in relations[parent]:
        print_descendants_helper(relations, child, 1)

def calculate_generation_distance_helper(relations, current, target, distance):
    if current == target:
        return distance
    # If the eprson has no descendant then there's no relationship
    if current not in relations:
        return -1

    # Iterates through each child and increase distance (to count) recursively
    for child in relations[current]:
        result = calculate_generation_distance_helper(relations, child, target, distance + 1)
        if result != -1:
            return result

    return -1

def calculate_generation_distance(relations, parent, child):
    # Calls the recursive helper method 
    distance = calculate_generation_distance_helper(relations, parent, child, 0) # Set the initial distance

    if distance == -1:
        print(f"{parent} and {child} are not related.")
    else:
        print(f"{parent} has a relationship with {child} at a distance of {distance} generations.")

# Main interface
def main():
    family_tree = create_family_tree()

    while True:
        print("=====================================================================")
        print("Enter family relations!")
        print("Format: <parent_name> <child_name>")
        print("Enter 'SELESAI' to finish.")

        # Get family relations from user input
        while True:
            input_data = input().split()

            if input_data[0] == "SELESAI":
                break

            parent, child = input_data
            add_relation(family_tree, parent, child)
        
        # Process user's action choice
        while True:
            print()
            print("=====================================================================")
            print("Welcome to Relation Finder! Options available:")
            print("1. CHECK_DESCENDANT")
            print("2. PRINT_DESCENDANTS")
            print("3. GENERATION_DISTANCE")
            print("4. EXIT")

            choice = int(input("Enter your choice: "))

            # Call the methods defined based on user's choice
            if choice == 1: 
                parent = input("Enter parent's name: ")
                child = input("Enter child's name: ")

                if check_descendant(family_tree, parent, child):
                    print(f"{child} is a descendant of {parent}.")
                else:
                    print(f"{child} is not a descendant of {parent}.")

            elif choice == 2:
                parent = input("Enter parent's name: ")
                print_descendants(family_tree, parent)

            elif choice == 3:
                parent = input("Enter parent's name: ")
                child = input("Enter child's name: ")

                calculate_generation_distance(family_tree, parent, child)

            elif choice == 4:
                print("Thank you for using Relation Finder!")
                return

            else:
                print("Invalid choice! Please re-input the choice.")

if __name__ == "__main__":
    main()
