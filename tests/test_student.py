import pytest
from school_schedule.student import Student

def test_add_class_increases_classes_length():
    name = "Diana"
    grade = "sophomore"
    classes = ["Astrophysics",
        "Underwater Basket Weaving",
        "How to Talk Like a Shark"]
    
    diana = Student(name, grade, classes)

    diana.add_class("Minnow Politics")

    assert len(diana.classes) == 4
    assert "Minnow Politics" in diana.classes