import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def splash_screen():
    ascii_text = r"""
  ____               _          ____      _            _       _              
 / ___|_ __ __ _  __| | ___    / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |  _| '__/ _` |/ _` |/ _ \  | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |_| | | | (_| | (_| |  __/  | |__| (_| | | (__| |_| | | (_| | || (_) | |   
 \____|_|  \__,_|\__,_|\___|   \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                                              
 _            ____                             ___   ___ 
| |__  _   _ / ___|_ __ ___  _   _ _ __       / _ \ / _ \
| '_ \| | | | |  _| '__/ _ \| | | | '_ \     | | | | (_) |
| |_) | |_| | |_| | | | (_) | |_| | |_) |    | |_| |\__, |
|_.__/ \__, |\____|_|  \___/ \__,_| .__/      \___/   /_/ 
       |___/                      |_|                     
"""
    start_time = time.time()
    while time.time() - start_time < 5:
        # Growing animation
        for i in range(1, 5):
            if time.time() - start_time >= 5: break
            clear_screen()
            print("\n" * i + ascii_text)
            time.sleep(0.15)
        # Shrinking animation
        for i in range(4, 0, -1):
            if time.time() - start_time >= 5: break
            clear_screen()
            print("\n" * i + ascii_text)
            time.sleep(0.15)
    clear_screen()

def calculate_grade():
    splash_screen()
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

                    # Display result in specified format
                    print("\n" + "-" * 30)
                    print(f"Name   : {name}")
                    print(f"Average: {average:.1f}")
                    print(f"Grade  : {grade}")
                    print("-" * 30)
                    
            except ValueError:
                print("Error: Please enter a valid numerical value for marks.")

        # Ask to continue or exit
        choice = input("\nType 'Exit' to stop or any other key to continue: ")
        if choice.strip().lower() == "exit":
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    calculate_grade()
