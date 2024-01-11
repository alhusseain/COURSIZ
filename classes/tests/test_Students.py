import unittest
from unittest.mock import patch
from Students import students

class TestStudents(unittest.TestCase):
    def setUp(self):
        self.student = students(1)
    
    @patch('databaseConnection.db')
    def test_addStudentToCourse(self, mock_db):
        mock_cursor = mock_db.cursor
        mock_cursor.fetchone.side_effect = [None, (10, 5)]
        
        # Test case when course does not exist
        result = self.student.addStudentToCourse("C001")
        self.assertFalse(result)
        
        # Test case when course exists and capacity is not reached
        result = self.student.addStudentToCourse("C002")
        self.assertTrue(result)
        mock_cursor.execute.assert_called_with("update Courses set Number_enrolled = ? where Course_Code = ?", (6, "C002"))
        mock_cursor.commit.assert_called()
        mock_cursor.execute.assert_called_with("insert into Enroll_in(Student_ID,Course_Code) values(?,?)", (1, "C002"))
        mock_cursor.commit.assert_called()
        
        # Test case when course exists and capacity is reached
        result = self.student.addStudentToCourse("C003")
        self.assertFalse(result)
    
    @patch('databaseConnection.db')
    def test_removeStudentFromCourse(self, mock_db):
        mock_cursor = mock_db.cursor
        
        self.student.Number_enrolled = 5
        
        self.student.removeStudentFromCourse("C001")
        mock_cursor.execute.assert_called_with("update Courses set Number_enrolled = ? where Course_Code = ?", (4, "C001"))
        mock_cursor.commit.assert_called()
        mock_cursor.execute.assert_called_with("delete from Enroll_in where Student_ID = ? and Course_Code = ?", (1, "C001"))
        mock_cursor.commit.assert_called()
    
    @patch('databaseConnection.db')
    def test_get_courses(self, mock_db):
        mock_cursor = mock_db.cursor
        mock_cursor.fetchall.return_value = [("C001",), ("C002",), ("C003",)]
        
        result = self.student.get_courses()
        self.assertEqual(result, ["C001", "C002", "C003"])

if __name__ == '__main__':
    unittest.main()