# Student Grade Processor
# This script calculates the average of three subject marks and determines 
# if a student has passed or failed based on a threshold of 40.

def main():
    # Prompt the user to input the student's name
    student_name = input("Enter the student's name: ")

    try:
        # Prompt for three separate subject marks and convert them to floats
        mark1 = float(input("Enter marks for Subject 1: "))
        mark2 = float(input("Enter marks for Subject 2: "))
        mark3 = float(input("Enter marks for Subject 3: "))

        # Calculate the arithmetic mean (average) of the three marks
        average_mark = (mark1 + mark2 + mark3) / 3

        # Determine pass/fail status
        # Pass if average is 40 or above, otherwise Fail
        if average_mark >= 40:
            status = "Pass"
        else:
            status = "Fail"

        # Display the final results in a readable format
        print("\n--- Student Result ---")
        print(f"Student Name: {student_name}")
        print(f"Average Mark: {average_mark:.2f}")
        print(f"Final Status: {status}")
        print("----------------------")

    except ValueError:
        # Handle cases where input is not a valid number
        print("Error: Please enter numeric values for the marks.")

if __name__ == "__main__":
    main()
