import os 


# Class representing a course in the system
class Course:
    def __init__(self, course_id, name, fee):
        # Initialize the course with a unique ID, name, and fee
        self.course_id = course_id
        self.name = name
        self.fee = fee

# Class representing a student in the system
class Student:
    def __init__(self, student_id, name, email):
        # Initialize the student with a unique ID, name, and email
        self.student_id = student_id
        self.name = name
        self.email = email
        # List to store courses the student is enrolled in
        self.courses = []
        # The student's total outstanding balance for all enrolled courses
        self.balance = 0

    # Method to enroll a student in a course
    def enroll(self, course):
        # If the student is not already enrolled in the course, enroll them
        if course not in self.courses:
            self.courses.append(course)
            self.balance += course.fee  # Update the balance by adding the course fee
        else:
            print(f"{self.name} is already enrolled in {course.name}")

    # Method to calculate the total fee for all enrolled courses
    def get_total_fee(self):
        return self.balance

# Class managing the overall registration system
class RegistrationSystem:
    def __init__(self):
        # List to store all available courses
        self.courses = []
        # Dictionary to store all registered students, keyed by their student ID
        self.students = {}

    # Method to add a new course to the system
    def add_course(self, course_id, name, fee):
        # Check if a course with the same ID already exists
        if any(course.course_id == course_id for course in self.courses):
            print(f"Course with ID {course_id} already exists.")
        else:
            # If the course doesn't exist, create it and add to the list of courses
            course = Course(course_id, name, fee)
            self.courses.append(course)

    # Method to register a new student
    def register_student(self, student_id, name, email):
        # Check if the student is already registered
        if student_id in self.students:
            print(f"Student with ID {student_id} already registered.")
        else:
            # If not, create a new student and add to the student registry
            student = Student(student_id, name, email)
            self.students[student_id] = student

    # Method to enroll a student in a course
    def enroll_in_course(self, student_id, course_id):
        # Retrieve the student object using student_id
        student = self.students.get(student_id)
        if not student:
            print(f"Student with ID {student_id} not found.")
            return
        
        # Retrieve the course object using course_id
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            print(f"Course with ID {course_id} not found.")
            return
        
        # Enroll the student in the course
        student.enroll(course)

    # Method to process a student's payment
    def calculate_payment(self, student_id):
        # Retrieve the student object using student_id
        student = self.students.get(student_id)
        if not student:
            print(f"Student with ID {student_id} not found.")
            return
        
        # Get the total outstanding balance
        balance = student.get_total_fee()
        if balance == 0:
            print(f"No outstanding balance for {student.name}.")
            return
        
        # Calculate the minimum payment (40% of the balance)
        min_payment = balance * 0.40
        print(f"Minimum payment is {min_payment}.")
        try:
            # Ask the user to input the payment amount
            payment = float(input(f"Enter payment amount for {student.name}: "))
            if payment < min_payment:
                print("Payment is below the minimum required.")
                return
            
            # Update the balance after payment
            student.balance -= payment
            print(f"The Remaining balance: {student.balance}")
        except ValueError:
            print("\nERROR!!!!")
            print("Invalid input! Please enter a numeric value for the payment.")

    # Method to check the current balance of a student
    def check_student_balance(self, student_id):
        # Retrieve the student object using student_id
        student = self.students.get(student_id)
        if not student:
            print("\n ERROR!!!!!!!")
            print(f"Student with ID {student_id} not found.")
        else:
            # Print the student's current balance
            print(f"{student.name}'s current balance: {student.balance}")

    # Method to display all available courses in the system
    def show_courses(self):
        # Check if there are any courses available
        if self.courses:
            for course in self.courses:
                print(f"ID: {course.course_id}, Name: {course.name}, Fee: {course.fee}")
        else:
            print("No courses available.")

    # Method to display all registered students
    def show_registered_students(self):
        # Check if there are any students registered
        if self.students:
            for student in self.students.values():
                print(f"ID: {student.student_id}, Name: {student.name}, Email: {student.email}")
        else:
            print("No students registered.")

    # Method to display all students enrolled in a specific course
    def show_students_in_course(self, course_id):
        # Retrieve the course object using course_id
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            print(f"Course with ID {course_id} not found.")
            return
        
        # Get the list of students enrolled in this course
        enrolled_students = [student.name for student in self.students.values() if course in student.courses]
        if enrolled_students:
            print(f"Student(s) enrolled in {course.name}: {', '.join(enrolled_students)}")
        else:
            print(f"No student(s) enrolled in {course.name}.")

# Main function that drives the menu and user interaction
def main():
    system = RegistrationSystem()

    # Infinite loop for the menu until the user chooses to exit
    while True:
        print("\nWELCOME To The Course Registration and Payment System\n")
        print("1. Add Course")
        print("2. Register Student")
        print("3. Enroll Student in Course")
        print("4. Calculate Payment")
        print("5. Check Student Balance")
        print("6. View Courses")
        print("7. View Registered Students")
        print("8. View Students in a Course")
        print("9. Exit")

        # Get user's choice from the menu
        choice = input("Choose an option: ")

        # Perform actions based on user's choice
        if choice == "1":
            # Add a new course
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            try:
                fee = float(input("Enter course fee: "))
                system.add_course(course_id, name, fee)
            except ValueError:
                print("Invalid fee input. Please enter a valid number.")
        elif choice == "2":
            # Register a new student
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            system.register_student(student_id, name, email)
        elif choice == "3":
            # Enroll a student in a course
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            system.enroll_in_course(student_id, course_id)
        elif choice == "4":
            # Process a student's payment
            student_id = input("Enter student ID: ")
            system.calculate_payment(student_id)
        elif choice == "5":
            # Check a student's balance
            student_id = input("Enter student ID: ")
            system.check_student_balance(student_id)
        elif choice == "6":
            # View all available courses
            system.show_courses()
        elif choice == "7":
            # View all registered students
            system.show_registered_students()
        elif choice == "8":
            # View all students in a specific course
            course_id = input("Enter course ID: ")
            system.show_students_in_course(course_id)
        elif choice == "9":
            # Exit the program
            print("\nExiting system, GOODBYE!!.")
            break
        else:
            print("\nERROR!!!!!")
            print("\nInvalid choice. Please try again.\n")

# Run the main function when the script is executed
if __name__ == "__main__":
