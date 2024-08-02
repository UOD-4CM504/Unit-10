import pytest
from main import Student, Records

def test_student_creation():
    student = Student("Joe", "Bloggs", 25, "j.bloggs@derby.ac.uk", 12345678)
    assert student.first_name == "Joe"
    assert student.surname == "Bloggs"
    assert student.age == 25
    assert student.email == "j.bloggs@derby.ac.uk"
    assert student.id == 12345678

def test_student_str():
    student = Student("Joe", "Bloggs", 25, "j.bloggs@derby.ac.uk", 12345678)
    expected_str = "Name: Joe Bloggs\nAge: 25\nEmail: j.bloggs@derby.ac.uk\nID: 12345678\n"
    assert str(student) == expected_str

def test_records_add_student():
    records = Records()
    student = Student("Joe", "Bloggs", 25, "j.bloggs@derby.ac.uk", 12345678)
    records.add_student(student)
    assert len(records._students) == 1
    assert records._students[0] == student

def test_records_add_student_from_list():
    records = Records()
    student1 = Student("Joe", "Bloggs", 25, "j.bloggs@derby.ac.uk", 12345678)
    student2 = Student("Ada", "Lovelace", 36, "a.lovelace@derby.ac.uk", 87654321)
    records.add_student_from_list([student1, student2])
    assert len(records._students) == 2
    assert records._students[0] == student1
    assert records._students[1] == student2

def test_records_str():
    records = Records()
    student1 = Student("Joe", "Bloggs", 25, "j.bloggs@derby.ac.uk", 12345678)
    student2 = Student("Ada", "Lovelace", 36, "a.lovelace@derby.ac.uk", 87654321)
    records.add_student_from_list([student1, student2])
    expected_str = (
        "Name: Joe Bloggs\nAge: 25\nEmail: j.bloggs@derby.ac.uk\nID: 12345678\n"
        "Name: Ada Lovelace\nAge: 36\nEmail: a.lovelace@derby.ac.uk\nID: 87654321\n"
    )
    assert str(records) == expected_str