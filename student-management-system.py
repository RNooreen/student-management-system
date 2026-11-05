
# Student Management System
# Author: Ruqayya Nooreen

# Class to represent an individual student
class Student:

    # Constructor to initialize student details
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course


# Class to manage student records
class StudentManagementSystem:

    # Constructor to initialize an empty student list
    def __init__(self):
        self.students = []

    # Method to get a valid positive integer
    def get_integer(self, message):

        while True:
            try:
                number = int(input(message))

                if number <= 0:
                    print("Please enter a positive number.")
                    continue

                return number

            except ValueError:
                print("Invalid input! Please enter a valid number.")

    # Method to check whether a Student ID already exists
    def is_duplicate(self, student_id):

        for student in self.students:

            if student.student_id == student_id:
                return True

        return False

    # Method to add a new student
    def add_student(self):

        # Keep asking until a unique Student ID is entered
        while True:

            student_id = self.get_integer("\nEnter Student ID: ")

            if self.is_duplicate(student_id):
                print("Student ID already exists. Please enter a different ID.")
            else:
                break

        name = input("Enter Student Name: ").strip()
        age = self.get_integer("Enter Student Age: ")
        course = input("Enter Student Course: ").strip()

        # Validate name and course
        if not name or not course:
            print("Name and course cannot be empty.")
            return

        # Create a Student object
        student = Student(student_id, name, age, course)

        # Add the student object to the list
        self.students.append(student)

        print("\nStudent added successfully!")

    # Method to display all student records
    def view_students(self):

        print("\n============ Student Records ============\n")

        # Check whether the student list is empty
        if not self.students:
            print("No student records found.")
            return

        # Display each student's details
        for student in self.students:

            print(f"Student ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Course: {student.course}")
            print("-" * 40)

    # Method to delete a student
    def delete_student(self):

        if not self.students:
            print("\nNo student records to delete.")
            return

        student_id = self.get_integer(
            "Enter the Student ID to delete: "
        )

        # Search for the student using the ID
        for student in self.students:

            if student.student_id == student_id:

                # Remove the student object from the list
                self.students.remove(student)

                print("Student deleted successfully!")
                return

        print("Student not found.")

    # Method to update student details
    def update_student(self):

        if not self.students:
            print("\nNo student records to update.")
            return

        student_id = self.get_integer(
            "Enter Student ID to update: "
        )

        # Search for the student
        for student in self.students:

            if student.student_id == student_id:

                print("\nStudent Found!")
                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Course")

                choice = input("Enter your choice: ")

                if choice == "1":

                    new_name = input("Enter new name: ").strip()

                    if new_name:
                        student.name = new_name
                        print("Name updated successfully!")
                    else:
                        print("Name cannot be empty.")

                elif choice == "2":

                    student.age = self.get_integer(
                        "Enter new age: "
                    )

                    print("Age updated successfully!")

                elif choice == "3":

                    new_course = input(
                        "Enter new course: "
                    ).strip()

                    if new_course:
                        student.course = new_course
                        print("Course updated successfully!")
                    else:
                        print("Course cannot be empty.")

                else:
                    print("Invalid choice.")

                return

        print("Student not found.")

    # Method to search for a student
    def search_student(self):

        if not self.students:
            print("\nNo student records available.")
            return

        student_id = self.get_integer(
            "Enter Student ID to search: "
        )

        # Search for the student using the ID
        for student in self.students:

            if student.student_id == student_id:

                print("\nStudent Found!")
                print("-" * 30)
                print(f"Student ID: {student.student_id}")
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Course: {student.course}")

                return

        print("Student not found.")


# Main function to run the application
def main():

    # Create an object of StudentManagementSystem
    sms = StudentManagementSystem()

    # Create sample student objects
    student1 = Student(101, "Ali", 20, "Python")
    student2 = Student(102, "Sara", 22, "Java")
    student3 = Student(103, "Ahmed", 21, "C++")
    student4 = Student(104, "Ayesha", 23, "Python")

    # Add sample students to the list
    sms.students.extend([
        student1, student2, student3, student4
    ])

    print("\nWelcome to Student Management System")

    # Display menu until the user chooses Exit
    while True:

        print("\n1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Update Student")
        print("5. Search Student")
        print("6. Exit")

        # Get menu choice with exception handling
        try:
            choice = int(input("\nEnter your choice: "))

        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Perform the selected operation
        if choice == 1:
            sms.add_student()

        elif choice == 2:
            sms.view_students()

        elif choice == 3:
            sms.delete_student()

        elif choice == 4:
            sms.update_student()

        elif choice == 5:
            sms.search_student()

        elif choice == 6:
            print("\nThank you for using Student Management System!")
            break

        else:
            print("Invalid Choice! Please select 1-6.")


# Program execution starts here
if __name__ == "__main__":
    main()
