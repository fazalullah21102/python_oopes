class Student:
    total_students = 0
    school_name = "ABC School"

    @classmethod
    def add_student(cls, name, age):
        cls.total_students += 1
        print(f"Student name  {name}, age {age}, added successfully.")
        print(f"Total students: {cls.total_students}")

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
        print(f"The school name is now changed to {cls.school_name}.")

# Example of usage:
Student.add_student("John", 15)
Student.change_school("XYZ School")
Student.add_student("Alice", 17)
