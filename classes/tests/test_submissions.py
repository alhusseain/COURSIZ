import unittest
from unittest.mock import MagicMock
from submissions import submissions

class TestSubmissions(unittest.TestCase):
    def setUp(self):
        self.submissions = submissions()

    def test_createSubmission(self):
        # Mock the database connection
        self.submissions.db = MagicMock()

        # Test case 1: Valid input
        upload_id = 1
        course_code = "CS101"
        out_of = 100
        deadline = "2022-01-01"
        self.submissions.createSubmission(upload_id, course_code, out_of, deadline)
        self.submissions.db.cursor.assert_called_with()
        self.submissions.db.cursor().execute.assert_called_with("insert into Sumbissions(Submission_ID,Deadline_Date) values(?,?)", (upload_id, deadline))
        self.submissions.db.connection.commit.assert_called()
        self.submissions.db.cursor().execute.assert_any_call("select distinct Student_ID from Enroll_in where Course_Code=?", (course_code,))
        self.submissions.db.cursor().execute.assert_any_call("insert into Submits(SubID,student_id,out_of) values(?,?,?)", (upload_id, student_id[0], out_of))
        self.assertEqual(self.submissions.db.cursor().execute.call_count, 2)
        self.submissions.db.connection.commit.assert_called()

        # Test case 2: Empty student IDs
        self.submissions.db.cursor().execute.return_value = []
        self.submissions.createSubmission(upload_id, course_code, out_of, deadline)
        self.submissions.db.cursor().execute.assert_called_with("select distinct Student_ID from Enroll_in where Course_Code=?", (course_code,))
        self.assertEqual(self.submissions.db.cursor().execute.call_count, 1)
        self.assertEqual(self.submissions.db.connection.commit.call_count, 1)

if __name__ == '__main__':
    unittest.main()