class Student:
    def __init__(self, first_name, surname, age, email, id):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.email = email
        self.id = id

    def __str__(self):
        return_string = ""
        return_string += f"Name: {self.first_name} {self.surname}\n"
        return_string += f"Age: {self.age}\n"
        return_string += f"Email: {self.email}\n"
        return_string += f"ID: {self.id}\n"
        return return_string


class Records:
    def __init__(self):
        self._students = []

    def __str__(self):
        return_string = ""
        for s in self._students:
            return_string += str(s)

        return return_string

    def add_student(self, student):
        self._students.append(student)

    def add_student_from_list(self, student_list):
        self._students.extend(student_list)


if __name__ == "__main__":
    records = Records()
    student_one = Student("Joe", "Bloggs", 25, "j.bloggs@derby.ac.uk", 12345678)
    student_two = Student("Ada", "Lovelace", 36, "a.lovelace@derby.ac.uk", 87654321)
    records.add_student_from_list([student_one, student_two])
    print(records)