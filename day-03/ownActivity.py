student_name = input("Enter student name: ")
age = input("Enter student age: ")

if age.isdigit():

    age = int(age)

    if age < 18:
        print("Student:", student_name)
        print("You are not allowed to attend.")

    elif age <= 25:
        print("Student:", student_name)
        print("You are allowed to attend.")
        print("Entrance fee: R50.00")

    else:
        print("Student:", student_name)
        print("You are allowed to attend.")
        print("Entrance fee: R100.00")

else:
    print("Invalid age! Please enter a valid number.")