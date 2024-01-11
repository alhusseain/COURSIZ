import unittest
from unittest.mock import patch
from Teacher import teacher

class TestTeacher(unittest.TestCase):

    def setUp(self):
        self.teacher = teacher(1)

    def test_sign_up(self):
        with patch('databaseConnection.db') as mock_db:
            self.teacher.sign_up()
            mock_db.cursor.execute.assert_called_with('INSERT INTO Teachers (teacher_id, course_code) VALUES (?, ?)', (1, self.teacher.course_code))
            mock_db.connection.commit.assert_called_once()

    def test_get_courses(self):
        with patch('databaseConnection.db') as mock_db:
            mock_db.cursor.fetchall.return_value = [('C001',), ('C002',)]
            courses = self.teacher.get_courses()
            mock_db.cursor.execute.assert_called_with("select Course_Code from Courses where TeacherID = ?", (1,))
            self.assertEqual(courses, ['C001', 'C002'])

    def test_get_courses_info(self):
        with patch('databaseConnection.db') as mock_db:
            mock_db.cursor.fetchall.return_value = [('C001', 'Math'), ('C002', 'Science')]
            course_codes, course_names = self.teacher.get_courses_info()
            mock_db.cursor.execute.assert_called_with('Select Course_Code,Name from Teachers t join Courses c on t.TeacherID=c.TeacherID where t.TeacherID=?', (1,))
            self.assertEqual(course_codes, ['C001', 'C002'])
            self.assertEqual(course_names, ['Math', 'Science'])

    def test_get_students_in_course(self):
        with patch('databaseConnection.db') as mock_db:
            mock_db.cursor.fetchall.side_effect = [[(1, 'John', 'Doe', 'john@example.com')], [(2, 'Jane', 'Smith', 'jane@example.com')]]
            self.teacher.course_codes = ['C001', 'C002']
            students = self.teacher.get_students_in_course()
            mock_db.cursor.execute.assert_called_with('Select s.Student_ID,u.First_Name,u.Last_Name,u.Email  from students s join Users u on u.Email=s.Email join Enroll_in E on s.Student_ID=E.Student_ID where E.Course_Code=?', ('C001',))
            self.assertEqual(students, [[(1, 'John', 'Doe', 'john@example.com')], [(2, 'Jane', 'Smith', 'jane@example.com')]])

if __name__ == '__main__':
    unittest.main()