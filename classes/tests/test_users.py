import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock

from users import users

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.user = users()
        self.user.sign_up_values('test@example.com', 'password', 'John', 'Doe', 'Student')

    def test_sign_up_values(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.password, 'password')
        self.assertEqual(self.user.First_name, 'John')
        self.assertEqual(self.user.Last_name, 'Doe')
        self.assertEqual(self.user.type, 'Student')
        self.assertIsInstance(self.user.today, datetime)

    def test_sign_in_values(self):
        self.user.sign_in_values('test@example.com', 'password')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.password, 'password')
        self.assertIsNone(self.user.First_name)
        self.assertIsNone(self.user.Last_name)
        self.assertIsNone(self.user.type)

    @patch('pyodbc.connect')
    def test_sign_up(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        self.user.sign_up()

        mock_cursor.execute.assert_called_with(
            "INSERT INTO dbo.Users(Email,First_Name,Last_Name,Password, User_Type,Account_creation_date) VALUES(?,?,?,?,?,?)",
            ('test@example.com', 'John', 'Doe', 'password', 'Student', self.user.today)
        )
        mock_cursor.commit.assert_called_once()

    @patch('pyodbc.connect')
    def test_sign_in_validation(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = ('test@example.com', 'password')
        mock_connect.return_value.cursor.return_value = mock_cursor

        self.user.email = 'test@example.com'
        self.user.password = 'password'

        self.assertTrue(self.user.sign_in_validation())

        mock_cursor.execute.assert_called_with(
            "SELECT * FROM dbo.Users WHERE Email = ? AND Password = ?",
            ('test@example.com', 'password')
        )
        mock_cursor.fetchone.assert_called_once()

    @patch('pyodbc.connect')
    def test_sign_in_get_data(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.fetchone.side_effect = [('Student',), ('John', 'Doe'), (1,)]
        mock_connect.return_value.cursor.return_value = mock_cursor

        self.user.email = 'test@example.com'

        result = self.user.sign_in_get_data()

        self.assertEqual(result, ('John', 'Doe', 1, 'Student'))

        mock_cursor.execute.assert_has_calls([
            MagicMock(('SELECT User_Type FROM dbo.Users WHERE Email = ?', ('test@example.com',))),
            MagicMock(('SELECT First_Name,Last_Name FROM dbo.Users WHERE Email = ?', ('test@example.com',))),
            MagicMock(('SELECT Student_ID FROM dbo.Students WHERE Email = ?', ('test@example.com',))),
        ])
        self.assertEqual(mock_cursor.fetchone.call_count, 3)

if __name__ == '__main__':
    unittest.main()