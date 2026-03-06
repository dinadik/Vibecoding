def calculate_grade():
    while True:
        # Ask for student name
        name = input("Enter student's name: ")
        
        # Constraint: Student name should be longer than 1 character
        if len(name) <= 1:
            print("Error: Student name must be longer than 1 character.")
        else:
            try:
                marks = []
                valid_marks = True
                for i in range(1, 4):
                    mark = float(input(f"Enter mark for subject {i}: "))
                    
                    # Constraint: Marks should be in the range 0-100 inclusive
                    if not (0 <= mark <= 100):
                        print(f"Error: Mark for subject {i} must be between 0 and 100.")
                        valid_marks = False
                        break
                    marks.append(mark)
                
                if valid_marks:
                    # Calculate the average
                    average = sum(marks) / len(marks)
                    
                    # Determine grade
                    if average >= 75:
                        grade = "A"
                    elif average >= 60:
                        grade = "B"
                    elif average >= 40:
                        grade = "C"
                    else:
                        grade = "Fail"

                    # Display result
                    print(f"\nStudent: {name}")
                    print(f"Average: {average:.2f}")
                    print(f"Grade: {grade}")
                    
            except ValueError:
                print("Error: Please enter a valid numerical value for marks.")

        # Ask to continue or exit
        choice = input("\nType 'Exit' to stop or any other key to continue: ")
        if choice.strip().lower() == "exit":
            break

if __name__ == "__main__":
    calculate_grade()
