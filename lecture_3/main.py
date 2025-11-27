def main():
 
    students = []

    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Show report (all students)")
        print("4. Find top performer")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            name = input("Enter student name: ").strip()
            
            student_exists = False
            for student in students:
                if student['name'] == name:
                    student_exists = True
                    break
            
            if student_exists:
                print(f"Student '{name}' already exists.")
            else:
                new_student = {"name": name, "grades": []}
                students.append(new_student)
                print(f"Student '{name}' added successfully.")

        elif choice == 2:
            name = input("Enter student name: ").strip()
            found_student = None
            
            for student in students:
                if student['name'] == name:
                    found_student = student
                    break
            
            if found_student:
                while True:
                    grade_input = input("Enter a grade (or 'done' to finish): ").strip()
                    
                    if grade_input.lower() == 'done':
                        break
                    
                    try:
                        grade = int(grade_input)
                        if 0 <= grade <= 100:
                            found_student['grades'].append(grade)
                        else:
                            print("Grade must be between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            else:
                print(f"Student '{name}' not found.")

        elif choice == 3:
            print("\n--- Student Report ---")
            averages = []
            
            for student in students:
                grades = student['grades']
                average = 0
                
                try:
                    average = sum(grades) / len(grades)
                    print(f"{student['name']}'s average grade is {average:.1f}.")
                    averages.append(average)
                except ZeroDivisionError:
                    print(f"{student['name']}'s average grade is N/A.")
            
            print("-" * 30)
            
            if averages:
                max_avg = max(averages)
                min_avg = min(averages)
                overall_avg = sum(averages) / len(averages)
                
                print(f"Max Average: {max_avg:.1f}")
                print(f"Min Average: {min_avg:.1f}")
                print(f"Overall Average: {overall_avg:.1f}")
            else:
                print("No grades available to calculate summary statistics.")

        elif choice == 4:
            students_with_grades = [s for s in students if len(s['grades']) > 0]
            
            if students_with_grades:
                top_student = max(students_with_grades, key=lambda s: sum(s['grades']) / len(s['grades']))
                
                top_avg = sum(top_student['grades']) / len(top_student['grades'])
                
                print(f"The student with the highest average is {top_student['name']} with a grade of {top_avg:.1f}.")
            else:
                print("No top student found (no grades added yet).")

        elif choice == 5:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()