CREATE TABLE Users
(
  Email VARCHAR NOT NULL,
  User_Type VARCHAR NOT NULL,
  Account_creation_date VARCHAR NOT NULL,
  PRIMARY KEY (Email)
);

CREATE TABLE Students
(
  Student_ID INT NOT NULL,
  First VARCHAR NOT NULL,
  Last VARCHAR NOT NULL,
  Year VARCHAR NOT NULL,
  attendanceRecord INT NOT NULL,
  GPA FLOAT NOT NULL,
  performancePoints INT NOT NULL,
  Email VARCHAR NOT NULL,
  PRIMARY KEY (Student_ID),
  FOREIGN KEY (Email) REFERENCES Users(Email)
);

CREATE TABLE Teachers
(
  FirstName VARCHAR NOT NULL,
  LastName VARCHAR NOT NULL,
  TeacherID INT NOT NULL,
  Email VARCHAR NOT NULL,
  PRIMARY KEY (TeacherID),
  FOREIGN KEY (Email) REFERENCES Users(Email)
);

CREATE TABLE SuperVisors
(
  FirstName VARCHAR NOT NULL,
  LastName VARCHAR NOT NULL,
  SupervisorID INT NOT NULL,
  Email VARCHAR NOT NULL,
  PRIMARY KEY (SupervisorID),
  FOREIGN KEY (Email) REFERENCES Users(Email)
);


CREATE TABLE Courses
(
  Name VARCHAR NOT NULL,
  Year INT NOT NULL,
  Semester VARCHAR NOT NULL,
  Course_Code VARCHAR NOT NULL,
  Capacity INT NOT NULL,
  Number_enrolled INT NOT NULL,
  TeacherID INT NOT NULL,
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
  Course_code VARCHAR NOT NULL,
  Date_of_Upload Date NOT NULL,
  Upload_header VARCHAR NOT NULL,
  Upload_type VARCHAR NOT NULL,
  Upload_description VARCHAR NOT NULL,
  Document_link VARCHAR NOT NULL,
  PRIMARY KEY (Upload_ID),
  FOREIGN KEY (Course_Code) REFERENCES Courses(Course_Code)
);

CREATE TABLE Sumbissions
(
  Submission_ID INT NOT NULL UNIQUE,
  Submission_type VARCHAR NOT NULL,
  Deadline_Date Date NOT NULL,
  Document_link VARCHAR NOT NULL,
  /*Upload_ID INT NOT NULL,*/
  /*PRIMARY KEY (Submission_ID),*/
  FOREIGN KEY (Submission_ID) REFERENCES Uploads(Upload_ID)
);

CREATE TABLE Announcements
(
  Submission_ID INT NOT NULL,
  Announcement VARCHAR NOT NULL,
  TeacherID INT ,
  Student_ID INT ,
  SupervisorID INT ,
  FOREIGN KEY (Submission_ID) REFERENCES Sumbissions(Submission_ID),
  FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID),
  FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID),
  FOREIGN KEY (SupervisorID) REFERENCES Supervisors(SupervisorID)
);

CREATE TABLE Enroll_in
(
  Student_ID INT NOT NULL,
  Course_Code VARCHAR NOT NULL,
  grade INT,
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
