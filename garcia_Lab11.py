grades = []

while True:
    grades_input = input("Enter grade of student (or type done to finish): ")
    
    if grades_input.lower() =='done':
        break
    
    try:
        grade = float(grades_input)
        
        if 40 < grade < 100:
            grades.append(grade)
        else:
            print("Please enter a grade between 40 and 100")
    except ValueError:
        print("Please enter a valid grade or 'done' to finish.")
        
if grades:
    average_grade = sum(grades) / len(grades)
    print(f"/ nAverage grade: {sum(grades)} / {len (grades)} = {average_grade:.2f}")
else:
    print("No grades entered.")

    
passing_grade = 75
passed_students = [grade for grade in grades if grade > passing_grade]
num_passed = len[passed_students]
total_students = len[grades]

if total_students > 0:
    passing_percentage = (num_passed / total_students)* 100
    print(f"/ nNumber of students passed: {num_passed} out of {total_students}")
    print(f"Passing percentage: {num_passed}/{total_students}= {passing_percentage:.2f}%")
else:
    print("No students to evaluate")
            
            