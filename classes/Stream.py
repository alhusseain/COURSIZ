class StreamItem:
    def __init__(self, title):
        self.title = title

    def display(self):
        print(f"Stream : {self.title}")


class Upload(StreamItem):
    def __init__(self, title, file):
        super().__init__(title)
        self.file = file

    def display(self):
        print(f"Upload: {self.title} - File: {self.file}")


class Announce(StreamItem):
    def __init__(self, title, message):
        super().__init__(title)
        self.message = message

    def display(self):
        print(f"Announcement: {self.title} - Message: {self.message}")


class Submit(StreamItem):
    def __init__(self, title, assignment):
        super().__init__(title)
        self.assignment = assignment

    def display(self):
        print(f"Submission: {self.title} - Assignment: {self.assignment}")


class Attendance(StreamItem):
    def __init__(self, title, student_name, present):
        super().__init__(title)
        self.student_name = student_name
        self.present = present

    def display(self):
        status = "Yes" if self.present else "No"
        print(f"Attendance: {self.title} - Student: {self.student_name} - Present: {status}")


class Stream:
    MAX_ITEMS = 10

    def __init__(self):
        self.items = []
        self.size = 0

    def add_item(self, item):
        if self.size < self.MAX_ITEMS:
            self.items.append(item)
            self.size += 1
        else:
            print("Stream is full. Cannot add more items.")

    def display_stream(self):
        for item in self.items:
            item.display()


class Teacher:
    def alert_submission(self, title, student_name, assignment_title):
        print(f"Alert: Teacher {title} - Student {student_name} submitted {assignment_title}.")

    def post_on_stream(self, item):
        item.display()

    def submit_attendance(self, title, student_name, present):
        attendance = Attendance(title, student_name, present)
        attendance.display()
        # Logic to store attendance record


def main():
    stream = Stream()
    teacher = Teacher()

    upload_type = input("Uploading? (Document, Announcement, Assignment): ")

    if upload_type == "Document" or upload_type == "Lecture":
        doc_title = input("Document title: ")
        doc_content = input("Document content: ")
        stream.add_item(Upload(doc_title, doc_content))
    elif upload_type == "Announcement":
        announce_title = input("Announcement title: ")
        announce_content = input("Announcement content: ")
        stream.add_item(Announce(announce_title, announce_content))
    elif upload_type == "Assignment":
        asg_title = input("Assignment title: ")
        asg_type = input("Assignment type: ")
        stream.add_item(Submit(asg_title, asg_type))
    else:
        print("Invalid upload type.")

    stream.display_stream()
    print("________________________________________")
    print("alert submittion ")
    teacher_name = input("Teacher name: ")
    student_name = input("Student name you want to alert: ")
    alert_sub = input("Assessment reminded: ")
    teacher.alert_submission(teacher_name, student_name, alert_sub)
    print("_____________________________________________")

    print("attendance tracker ")
    class_name = input("Class name: ")
    student_name = input("Student name: ")
    attended = input("Attended? (True/False): ").lower() == "true"
    teacher.submit_attendance(class_name, student_name, attended)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
