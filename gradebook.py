# Initial Gradebook List for computer science class
gradebook = [100, "Variables Test", 75, "Variables HW"]

# Function to print grades
def print_grades():
    print("Current Gradebook: " + str(gradebook))

# function to amend the gradebook
def amend_gradebook(operation, grade_input, assignment_input):
    if(operation == "add"):
        gradebook.append(assignment_input)
        gradebook.append(int(grade_input))
    elif(operation == "remove"):
        assignment = ""
        if(assignment in gradebook and int(grade_input) in gradebook):
            gradebook.remove(assignment_input)
            gradebook.remove(int(grade_input))
        else:
            print("Assignment or grade not found in gradebook")
    else:
        print_grades()

# main function
def main():
    print("Welcome to John's CS Gradebook. ")
    while True:
        user_input = input("What would you like to do? [Add] or [Remove] Grade or [Print] or type [Exit] to quit: ").lower()
        if(user_input == "add"):
            assignment_input = input("Please enter the assignment name: ")
            grade_input = input("Please enter the grade: ")
            amend_gradebook("add", grade_input, assignment_input)
        elif(user_input == "remove"):
            assignment_input = input("Please enter the assignment name you want to remove: ")
            grade_input = input("Please enter the grade you want to remove: ")
            amend_gradebook("remove", grade_input, assignment_input)
        elif(user_input == "print"):
            print_grades()
        elif(user_input == "exit"):
            print("Exiting Gradebook")
            break

#running the main function
main()  
