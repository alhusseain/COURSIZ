CREATE TABLE Users
(
  First_Name VARCHAR(MAX),
  Last_Name  VARCHAR(MAX),
  Email VARCHAR(MAX) NOT NULL,
  User_Type VARCHAR(MAX) NOT NULL,
  Account_creation_date VARCHAR(MAX) NOT NULL,
  PRIMARY KEY (Email)
);

CREATE TABLE Students
(
  Student_ID INT NOT NULL,
  /*First VARCHAR NOT NULL,
  Last VARCHAR NOT NULL,*/
  Year VARCHAR(MAX) ,
  attendanceRecord INT,
  GPA FLOAT ,
  performancePoints INT ,
  Email VARCHAR(MAX) NOT NULL,
  PRIMARY KEY (Student_ID),
  FOREIGN KEY (Email) REFERENCES Users(Email)
);

CREATE TABLE Teachers
(
  /*FirstName VARCHAR NOT NULL,
  LastName VARCHAR NOT NULL,*/
  TeacherID INT NOT NULL,
  Email VARCHAR(MAX) NOT NULL,
  PRIMARY KEY (TeacherID),
  FOREIGN KEY (Email) REFERENCES Users(Email)
);

CREATE TABLE SuperVisors
(
  /*FirstName VARCHAR NOT NULL,
  LastName VARCHAR NOT NULL,*/
  SupervisorID INT NOT NULL,
  Email VARCHAR(MAX) NOT NULL,
  PRIMARY KEY (SupervisorID),
  FOREIGN KEY (Email) REFERENCES Users(Email)
);


CREATE TABLE Courses
(
  Name VARCHAR(MAX) NOT NULL,
  Year INT NOT NULL,
  Semester VARCHAR(MAX) ,
  Course_Code VARCHAR(MAX) NOT NULL,
  Capacity INT ,
  Number_enrolled INT ,
  TeacherID INT ,
  /*SupervisorID INT NOT NULL,*/
  /*Student_ID INT NOT NULL,*/
  PRIMARY KEY (Course_Code),
  FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID),
  /*FOREIGN KEY (SupervisorID) REFERENCES SuperVisors(SupervisorID), */
 /* FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID)*/
);

CREATE TABLE Uploads
(
  Upload_ID INT NOT NULL,
  Course_code VARCHAR(MAX) NOT NULL,
  Date_of_Upload Date NOT NULL,
  Upload_header VARCHAR(MAX) NOT NULL,
  Upload_type VARCHAR(MAX) NOT NULL,
  Upload_description VARCHAR(MAX),
  Document_link VARCHAR(MAX),
  PRIMARY KEY (Upload_ID),
  FOREIGN KEY (Course_Code) REFERENCES Courses(Course_Code)
);

CREATE TABLE Sumbissions
(
  Submission_ID INT NOT NULL UNIQUE,
  Submission_type VARCHAR(MAX) NOT NULL,
  Deadline_Date Date,
  Document_link VARCHAR(MAX),
  /*Upload_ID INT NOT NULL,*/
  /*PRIMARY KEY (Submission_ID),*/
  FOREIGN KEY (Submission_ID) REFERENCES Uploads(Upload_ID)
);

CREATE TABLE Announcements
(
  Submission_ID INT NOT NULL,
  Announcement VARCHAR(MAX),
  TeacherID INT ,
  Student_ID INT ,
  SupervisorID INT ,
  Document_link VARCHAR(MAX),
  FOREIGN KEY (Submission_ID) REFERENCES Sumbissions(Submission_ID),
  FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID),
  FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID),
  FOREIGN KEY (SupervisorID) REFERENCES Supervisors(SupervisorID)
);

CREATE TABLE Enroll_in
(
  Student_ID INT NOT NULL,
  Course_Code VARCHAR(MAX) NOT NULL,
  final_grade float,
  PRIMARY KEY (Student_ID, Course_Code),
  FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID),
  FOREIGN KEY (Course_Code) REFERENCES Courses(Course_Code)
);

/*CREATE TABLE Enroll
(
  grade INT NOT NULL,
  Student_ID INT NOT NULL,
  Course_Code VARCHAR NOT NULL,
  PRIMARY KEY (grade, Student_ID, Course_Code),
  FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID),
  FOREIGN KEY (Course_Code) REFERENCES Courses(Course_Code)
);*/
