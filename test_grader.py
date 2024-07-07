import unittest
from grader import Grader

gr = Grader()

class Test(unittest.TestCase):
    # Test with number outside of range 0-100 should return true
    def test_grade_info_for_input_error(self):
        name = "student"
        assignment = "AMths"
        grade = 1000
        self.assertEqual(
            gr.gradeInfo(name, assignment, grade),
            "You did not entered a grade number between 0 and 100.",
        )

    # Test for grade to return an A
    def test_grade_info_for_a(self):
        name = "student1"
        assignment = "Maths"
        grade = 90
        self.assertEqual(
            gr.gradeInfo(name, assignment, grade),
            "Hello student1\nYour letter grade for Maths assignment is as follows: A\nAssignment details:\nYou have met most or all of the assignment's requirements.",
        )

    # Test for grade to return an B
    def test_grade_info_for_b(self):
        name = "student2"
        assignment = "Science 104"
        grade = 80
        self.assertEqual(
            gr.gradeInfo(name, assignment, grade),
            "Hello student2\nYour letter grade for Science 104 assignment is as follows: B\nAssignment details:\nYou have met most of the assignment's requirements.",
        )

    # Test for grade to return an C
    def test_grade_info_for_c(self):
        name = "student3"
        assignment = "Cooking 404"
        grade = 70
        self.assertEqual(
            gr.gradeInfo(name, assignment, grade),
            "Hello student3\nYour letter grade for Cooking 404 assignment is as follows: C\nAssignment details:\nYou have met many of the assignment's requirements.",
        )

    # Test for grade to return an D
    def test_grade_info_for_d(self):
        name = "student4"
        assignment = "Music Theory"
        grade = 60
        self.assertEqual(
            gr.gradeInfo(name, assignment, grade),
            "Hello student4\nYour letter grade for Music Theory assignment is as follows: D\nAssignment details:\nYou have met some of the assignment's requirements.",
        )

    # Test for grade to check if student failed
    def test_grade_info_for_fail(self):
        name = "student5"
        assignment = "Calc XIV"
        grade = 45
        self.assertFalse(gr.gradeInfo(name, assignment, grade))

    # Test for grade to check if student passed
    def test_grade_info_for_pass(self):
        name = "student6"
        assignment = "Sleep 101"
        grade = 100
        self.assertIsNotNone(gr.gradeInfo(name, assignment, grade))

    # Test add to student roster for student Pedro
    def test_add_student(self):
        newStudent = {"name": "Pedro", "favoriteColor": "navy"}
        gr.addStudent(newStudent)
        self.assertIn(newStudent, gr.students)

    # Test student roster for student mike
    def test_students(self):
        self.assertListEqual(
            [
                {"name": "mike", "favoriteColor": "blue"},
                {"name": "john", "favoriteColor": "red"},
                {"name": "alice", "favoriteColor": "green"},
                {"name": "sarah", "favoriteColor": "yellow"},
                {"name": "david", "favoriteColor": "purple"},
                {"name": "emily", "favoriteColor": "orange"},
                {"name": "ben", "favoriteColor": "pink"},
                {"name": "chloe", "favoriteColor": "black"},
                {"name": "liam", "favoriteColor": "white"},
                {"name": "noah", "favoriteColor": "brown"},
                {"name": "Pedro", "favoriteColor": "navy"},
            ],
            gr.showStudents(),
        )
