CREATE TABLE Users
(
  FirstName VARCHAR(50) NOT NULL,
  LastName VARCHAR(50) NOT NULL,
  Email VARCHAR(100) NOT NULL,
  User_Type VARCHAR(50) NOT NULL,
  Account_creation_date VARCHAR(50) NOT NULL,
  PRIMARY KEY (Email)
);

CREATE TABLE Students
(
  Student_ID INT NOT NULL,
  FirstName VARCHAR(50) NOT NULL,
  LastName VARCHAR(50) NOT NULL,
  Year int NOT NULL,
  attendanceRecord INT NOT NULL,
  GPA FLOAT NOT NULL,
  performancePoints INT NOT NULL,
  Email VARCHAR(100) NOT NULL,
  PRIMARY KEY (Student_ID),
  FOREIGN KEY (Email) REFERENCES Users(Email),
  FOREIGN KEY (FirstName) REFERENCES Users(FirstName),
  FOREIGN KEY (LastName) REFERENCES Users(LastName)
);

CREATE TABLE Teachers
(
  FirstName VARCHAR(50) NOT NULL,
  LastName VARCHAR(50) NOT NULL,
  TeacherID INT NOT NULL,
  Email VARCHAR(100) NOT NULL,
  PRIMARY KEY (TeacherID),
  FOREIGN KEY (Email) REFERENCES Users(Email),
  FOREIGN KEY (FirstName) REFERENCES Users(FirstName),
  FOREIGN KEY (LastName) REFERENCES Users(LastName)
);

CREATE TABLE SuperVisors
(
  FirstName VARCHAR(50) NOT NULL,
  LastName VARCHAR(50) NOT NULL,
  SupervisorID INT NOT NULL,
  Email VARCHAR(100) NOT NULL,
  PRIMARY KEY (SupervisorID),
  FOREIGN KEY (Email) REFERENCES Users(Email)
);


CREATE TABLE Courses
(
  courseName VARCHAR(50) NOT NULL,
  yearTeached INT NOT NULL,
  Semester VARCHAR(50) NOT NULL,
  Course_Code VARCHAR(50) NOT NULL,
  Capacity INT NOT NULL,
  Number_enrolled INT NOT NULL,
  PRIMARY KEY (Course_Code)
);

CREATE TABLE Uploads
(
  Upload_ID INT NOT NULL,
  Course_code VARCHAR(50) NOT NULL,
  Date_of_Upload Date NOT NULL,
  Upload_header VARCHAR(50) NOT NULL,
  Upload_type VARCHAR(50) NOT NULL,
  Upload_description VARCHAR(50000) NOT NULL,
  Document_link VARCHAR(500) NOT NULL,
  professorID INT ,
  SupervisorID INT ,
  PRIMARY KEY (Upload_ID),
  FOREIGN KEY (Course_Code) REFERENCES Courses(Course_Code),
  FOREIGN KEY (professorID) REFERENCES Teachers(TeacherID)
);

CREATE TABLE Sumbissions
(
  Submission_ID INT NOT NULL UNIQUE,
  Document_link VARCHAR(500) NOT NULL,
  Student_ID INT NOT NULL,
  Upload_ID INT NOT NULL,
  PRIMARY KEY (Submission_ID),
  FOREIGN KEY (Upload_ID) REFERENCES Uploads(Upload_ID),
  FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID),
);

CREATE TABLE Announcements
(
  AnnouncementID INT NOT NULL,
  Announcement VARCHAR(50000) NOT NULL,
  TeacherID INT ,
  Student_ID INT ,
  SupervisorID INT,
  FOREIGN KEY (AnnouncementID) REFERENCES Uploads(Upload_ID),
  FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID),
  FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID),
  FOREIGN KEY (SupervisorID) REFERENCES Supervisors(SupervisorID)
);

CREATE TABLE Enroll_in
(
  Student_ID INT NOT NULL,
  Course_Code VARCHAR(50) NOT NULL,
  PRIMARY KEY (Student_ID, Course_Code),
  FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID),
  FOREIGN KEY (Course_Code) REFERENCES Courses(Course_Code)
);

create table teaches
(
  TeacherID INT NOT NULL,
  Course_Code VARCHAR(50) NOT NULL,
  PRIMARY KEY (TeacherID, Course_Code),
  FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID),
  FOREIGN KEY (Course_Code) REFERENCES Courses(Course_Code)
);
