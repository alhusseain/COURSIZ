import unittest
from unittest.mock import MagicMock
from datetime import datetime
from Upload import upload

class TestUpload(unittest.TestCase):
    def setUp(self):
        self.upload_obj = upload()
        self.upload_obj.db = MagicMock()

    def test_upload_info(self):
        course_code = "CSCI101"
        self.upload_obj.db.cursor.fetchall.return_value = [(1,), (2,), (3,)]
        self.upload_obj.upload_info(course_code)
        self.assertEqual(self.upload_obj.up_id, [1, 2, 3])
        self.upload_obj.db.cursor.execute.assert_called_with("select Upload_ID from Uploads where Course_code = ?", course_code)

        # Add more assertions for other attributes

    def test_insert_upload(self):
        header = "Assignment 1"
        type = "Assignment"
        description = "Complete exercises 1-5"
        link = "https://example.com/assignment1"
        course_code = "CSCI101"
        today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.upload_obj.db.cursor.fetchone.return_value = (5,)
        self.upload_obj.today = today
        self.upload_obj.insert_upload(header, type, description, link, course_code)
        self.upload_obj.db.cursor.execute.assert_called_with(
            "INSERT INTO Uploads(Upload_ID,Upload_header,Upload_type,Upload_description,Document_link,Course_code,Date_of_Upload) VALUES(?,?,?,?,?,?,?)",
            (6, header, type, description, link, course_code, today)
        )
        self.upload_obj.db.cursor.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()