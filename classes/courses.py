import databaseConnection
import students
import professors
query = connection.cursor()


class courses(students, professors):
    def __init__(self, courseName, yearTeached, Semester, Course_Code, Capacity, Number_enrolled):
        self.courseName = courseName
        self.yearTeached = yearTeached
        self.Semester = Semester
        self.Course_Code = Course_Code
        self.Capacity = Capacity
        self.Number_enrolled = Number_enrolled
    
    def createCourse(self, courseName, yearTeached, Semester, Course_Code, Capacity, Number_enrolled):
        query.excute('''insert into Courses(courseName, yearTeached, Semester, Course_Code, Capacity, Number_enrolled)
        values (?, ?, ?, ?, ?, ?)''', (courseName, yearTeached, Semester, Course_Code, Capacity, Number_enrolled))
        query.commit()
    
    def deleteCourse(self, courseName, yearTeached, Semester, Course_Code, Capacity, Number_enrolled):
        query.excute('''delete from Courses where courseName = ? and yearTeached = ? and Semester = ? and Course_Code = ? and Capacity = ? and Number_enrolled = ?''', (courseName, yearTeached, Semester, Course_Code, Capacity, Number_enrolled))
        query.commit()
    
    def addStudentToCourse(self, student, Course_Code):
        query.excute('''update Courses set Number_enrolled = ? where Course_Code = ?''', (Number_enrolled + 1 , Course_Code))
        query.commit()
        query.excute('''insert into Enroll_in set Student_ID = ?, Course_Code = ?, grade = ?''', (student.studentID, Course_Code, NULL))
        query.commit()
    
    def removeStudentFromCourse(self, student, Course_Code):
        query.excute('''update Courses set Number_enrolled = ? where Course_Code = ?''', (Number_enrolled - 1 , Course_Code))
        query.commit()
        query.excute('''delete from Enroll_in where Student_ID = ? and Course_Code = ?''', (student.studentID, Course_Code))
        query.commit()
    
    
    
        
    