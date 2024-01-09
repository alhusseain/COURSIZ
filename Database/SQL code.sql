USE [master]
GO
/****** Object:  Database [Coursiz]    Script Date: 23/12/2023 13:45:23 ******/
CREATE DATABASE [Coursiz]
CONTAINMENT = NONE
GO
ALTER DATABASE [Coursiz] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Coursiz].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Coursiz] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Coursiz] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Coursiz] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Coursiz] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Coursiz] SET ARITHABORT OFF 
GO
ALTER DATABASE [Coursiz] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Coursiz] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Coursiz] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Coursiz] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Coursiz] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Coursiz] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Coursiz] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Coursiz] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Coursiz] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Coursiz] SET  DISABLE_BROKER 
GO
ALTER DATABASE [Coursiz] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Coursiz] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Coursiz] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Coursiz] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Coursiz] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Coursiz] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Coursiz] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Coursiz] SET RECOVERY FULL 
GO
ALTER DATABASE [Coursiz] SET  MULTI_USER 
GO
ALTER DATABASE [Coursiz] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Coursiz] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Coursiz] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Coursiz] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Coursiz] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [Coursiz] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'Coursiz', N'ON'
GO
ALTER DATABASE [Coursiz] SET QUERY_STORE = ON
GO
ALTER DATABASE [Coursiz] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [Coursiz]
GO
/****** Object:  Table [dbo].[Announcements]    Script Date: 23/12/2023 13:45:23 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Announcements](
	[Submission_ID] [int] NOT NULL,
	[Announcement] [varchar](max) NULL,
	[TeacherID] [int] NULL,
	[Student_ID] [int] NULL,
	[SupervisorID] [int] NULL,
	[Document_link] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Courses]    Script Date: 23/12/2023 13:45:23 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Courses](
	[Name] [nvarchar](100) NOT NULL,
	[Year] [int] NOT NULL,
	[Semester] [varchar](max) NULL,
	[Course_Code] [nvarchar](100) NOT NULL,
	[Capacity] [int] NULL,
	[Number_enrolled] [int] NULL,
	[TeacherID] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[Course_Code] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Enroll_in]    Script Date: 23/12/2023 13:45:23 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Enroll_in](
	[Student_ID] [int] NOT NULL,
	[Course_Code] [nvarchar](100) NOT NULL,
	[final_grade] [float] NULL,
PRIMARY KEY CLUSTERED 
(
	[Student_ID] ASC,
	[Course_Code] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Students]    Script Date: 23/12/2023 13:45:23 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Students](
	[Student_ID] [int] NOT NULL,
	[Year] [varchar](max) NULL,
	[attendanceRecord] [int] NULL,
	[GPA] [float] NULL,
	[performancePoints] [int] NULL,
	[Email] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[Student_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Sumbissions]    Script Date: 23/12/2023 13:45:23 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Sumbissions](
	[Submission_ID] [int] NOT NULL,
	[Submission_type] [varchar](max) NOT NULL,
	[Document_link] [varchar](max) NULL,
UNIQUE NONCLUSTERED 
(
	[Submission_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SuperVisors]    Script Date: 23/12/2023 13:45:23 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SuperVisors](
	[SupervisorID] [int] NOT NULL,
	[Email] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[SupervisorID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Teachers]    Script Date: 23/12/2023 13:45:23 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Teachers](
	[TeacherID] [int] NOT NULL,
	[Email] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[TeacherID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Uploads]    Script Date: 23/12/2023 13:45:23 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Uploads](
	[Upload_ID] [int] NOT NULL,
	[Course_code] [nvarchar](100) NOT NULL,
	[Upload_header] [varchar](max) NOT NULL,
	[Upload_type] [varchar](max) NOT NULL,
	[Upload_description] [varchar](max) NULL,
	[Document_link] [varchar](max) NULL,
	[Date_of_Upload] [varchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[Upload_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Users]    Script Date: 23/12/2023 13:45:23 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Users](
	[First_Name] [varchar](max) NULL,
	[Last_Name] [varchar](max) NULL,
	[Email] [nvarchar](100) NOT NULL,
	[User_Type] [varchar](max) NOT NULL,
	[Password] [varchar](max) NULL,
	[Account_creation_date] [varchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[Email] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[Announcements]  WITH CHECK ADD FOREIGN KEY([Student_ID])
REFERENCES [dbo].[Students] ([Student_ID])
GO
ALTER TABLE Sumbissions
ADD CONSTRAINT studentID_FK
FOREIGN KEY (studentID) REFERENCES Students(Student_ID);
GO
ALTER TABLE [dbo].[Announcements]  WITH CHECK ADD FOREIGN KEY([Submission_ID])
REFERENCES [dbo].[Sumbissions] ([Submission_ID])
GO
ALTER TABLE [dbo].[Announcements]  WITH CHECK ADD FOREIGN KEY([SupervisorID])
REFERENCES [dbo].[SuperVisors] ([SupervisorID])
GO
ALTER TABLE [dbo].[Announcements]  WITH CHECK ADD FOREIGN KEY([TeacherID])
REFERENCES [dbo].[Teachers] ([TeacherID])
GO
ALTER TABLE [dbo].[Courses]  WITH CHECK ADD FOREIGN KEY([TeacherID])
REFERENCES [dbo].[Teachers] ([TeacherID])
GO
ALTER TABLE [dbo].[Enroll_in]  WITH CHECK ADD FOREIGN KEY([Course_Code])
REFERENCES [dbo].[Courses] ([Course_Code])
GO
ALTER TABLE [dbo].[Enroll_in]  WITH CHECK ADD FOREIGN KEY([Student_ID])
REFERENCES [dbo].[Students] ([Student_ID])
GO
ALTER TABLE [dbo].[Students]  WITH CHECK ADD FOREIGN KEY([Email])
REFERENCES [dbo].[Users] ([Email])
GO
ALTER TABLE [dbo].[Sumbissions]  WITH CHECK ADD FOREIGN KEY([Submission_ID])
REFERENCES [dbo].[Uploads] ([Upload_ID])
GO
ALTER TABLE [dbo].[SuperVisors]  WITH CHECK ADD FOREIGN KEY([Email])
REFERENCES [dbo].[Users] ([Email])
GO
ALTER TABLE [dbo].[Teachers]  WITH CHECK ADD FOREIGN KEY([Email])
REFERENCES [dbo].[Users] ([Email])
GO
ALTER TABLE [dbo].[Uploads]  WITH CHECK ADD FOREIGN KEY([Course_code])
REFERENCES [dbo].[Courses] ([Course_Code])
GO
USE [master]
GO
ALTER DATABASE [Coursiz] SET  READ_WRITE 
GO
