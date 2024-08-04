class Student:
    pass


class Records:
    pass


if __name__ == "__main__":
    records = Records()
    student_one = Student("Joe", "Bloggs", 25, "j.bloggs@derby.ac.uk", 12345678)
    student_two = Student("Ada", "Lovelace", 36, "a.lovelace@derby.ac.uk",
                          87654321)
    records.add_student_from_list([student_one, student_two])
    print(records)
