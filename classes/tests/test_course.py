import unittest
from unittest.mock import patch
from course import Course_class

class TestCourseClass(unittest.TestCase):
    def setUp(self):
        self.course = Course_class("Math", 2022, "Fall", 30, "John Doe")

    def test_createCourse_validTeacher(self):
        with patch('pyodbc.Cursor') as mock_cursor:
            mock_cursor.fetchone.return_value = ['john.doe@example.com']
            result = self.course.createCourse()
            self.assertTrue(result)

    def test_createCourse_invalidTeacher(self):
        with patch('pyodbc.Cursor') as mock_cursor:
            mock_cursor.fetchone.return_value = None
            result = self.course.createCourse()
            self.assertFalse(result)

    def test_createCourse_invalidTeacherName(self):
        self.course.teacher_name = "John"
        result = self.course.createCourse()
        self.assertFalse(result)

    def test_deleteCourse(self):
        with patch('pyodbc.Cursor') as mock_cursor:
            result = self.course.deleteCourse("Cs1")
            self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()