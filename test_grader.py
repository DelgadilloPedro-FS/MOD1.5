import unittest
from grader import Grader

gr = Grader()

class Test(unittest.TestCase):

    def test_gradeInfo(self):
        name = 'student'
        assignment='AMths'
        grade=1000
        self.assertEqual(gr.gradeInfo(name,assignment,grade),"You did not entered a grade number between 0 and 100.")
    
    def test_gradeInfoForA(self):
        name = 'student1'
        assignment='Maths'
        grade=90
        self.assertEqual(gr.gradeInfo(name,assignment,grade), "Hello student1\nYour letter grade for Maths assignment is as follows: A\nAssignment details:\nYou have met most or all of the assignment's requirements.")