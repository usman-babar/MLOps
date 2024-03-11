import pytest
from main import StudentsInMLOps

@pytest.fixture
def students_instance():
    return StudentsInMLOps()

def test_enroll_students(students_instance):
    students_instance.enrollStudents(5)
    assert students_instance.getTotalStrength() == 5

def test_drop_students(students_instance):
    students_instance.enrollStudents(10)
    students_instance.dropStudents(3)
    assert students_instance.getTotalStrength() == 7

def test_get_class_name(students_instance):
    assert students_instance.getClassName() == "StudentsInMLOps"

