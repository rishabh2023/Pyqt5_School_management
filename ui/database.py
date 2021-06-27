import sqlite3

try:
    sqliteConnection = sqlite3.connect('Schooldb_01.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    
    # Students Details Table Creation query
    student_details_Query = """CREATE TABLE IF NOT EXISTS studetails_01(
        ADDMISSION_NO INT(4) PRIMARY KEY,
        STUDENT_NAME VARCHAR(50) NOT NULL,
        FATHERS_NAME VARCHAR(50) NOT NULL,
        MOTHERS_NAME VARCHAR(50) NOT NULL,
        DOB DATE NOT NULL,
        GENDER CHAR(1) NOT NULL,
        ADDMISSION_MODE VARCHAR(6) NOT NULL,
        TRANSPORT_MODE VARCHAR(8) NOT NULL,
        TRANSPORT_DETAILS VARCHAR(10) NOT NULL,
        ACCOUNT_NO VARCHAR(16) NOT NULL,
        AADHAR_NO VARCHARCHAR(12) NOT NULL,
        SSSMID_NO VARCHAR(9) NOT NULL,
        SCHOLAR_NO VARCHAR(10) NOT NULL,
        EMAIL VARCHAR(20) NOT NULL,
        MOBILE_NO CHAR(10) NOT NULL,
        ADDRESS VARCHAR(50) NOT NULL)"""


    students_fees_Query = """CREATE TABLE IF NOT EXISTS studfees_01(
        TRANSACTION_NO INT(9) PRIMARY KEY,
        ADDMISSION_NO INT(4),
        APRIL INT(5) DEFAULT 0,
        APRIL_DATE DATE  DEFAULT '0000-00-00',
        JULY INT(5) DEFAULT 0,
        JULY_DATE DATE DEFAULT '0000-00-00',
        AUG INT(5) DEFAULT 0,
        AUG_DATE DATE DEFAULT '0000-00-00',
        SEPT INT(5) DEFAULT 0,
        SEPT_DATE DATE DEFAULT '0000-00-00',
        NOV INT(5) DEFAULT 0,
        NOV_DATE DATE DEFAULT '0000-00-00',
        DEC INT(5) DEFAULT 0,
        DEC_DATE DATE  DEFAULT '0000-00-00',
        JAN INT(5) DEFAULT 0,
        JAN_DATE DATE DEFAULT '0000-00-00',
        FEB INT(5) DEFAULT 0,
        FEB_DATE DATE DEFAULT '0000-00-00',
        MARCH INT(5) DEFAULT 0, 
        MARCH_DATE DATE DEFAULT '0000-00-00',
        TRANSPORT_FEES INT(4) DEFAULT 0,
        ANNUAL_FEES INT(5) DEFAULT 0,
        TOTAL_PAID INT(5) DEFAULT 0,
        FEES_DUE INT(5) DEFAULT 0,
        FOREIGN KEY(ADDMISSION_NO) REFERENCES studetails_01(ADDMISSION_NO)
        )"""
    
    fees_list_Query = """CREATE TABLE IF NOT EXISTS feeslist_01(
        CLASSES VARCHAR(6), 
        CLASS_FESS INT(5),
        NO_OF_STUDENTS INT(5))"""

    transport_list_Query = """CREATE TABLE IF NOT EXISTS transportlist_01(
        ORIGIN VARCHAR(10), 
        TRANSPORT_FESS INT(5),
        NO_OF_STUDENTS INT(5))"""
    
    backup_data_Query =  """CREATE TABLE IF NOT EXISTS studetails_01(
        ADDMISSION_NO INT(4) NOT NULL,
        STUDENT_NAME VARCHAR(50) NOT NULL,
        FATHERS_NAME VARCHAR(50) NOT NULL,
        MOTHERS_NAME VARCHAR(50) NOT NULL,
        DOB DATE NOT NULL,
        GENDER CHAR(1) NOT NULL,
        ADDMISSION_MODE VARCHAR(6) NOT NULL,
        TRANSPORT_MODE VARCHAR(8) NOT NULL,
        TRANSPORT_DETAILS VARCHAR(10) NOT NULL,
        ACCOUNT_NO VARCHAR(16) NOT NULL,
        AADHAR_NO VARCHARCHAR(12) NOT NULL,
        SSSMID_NO VARCHAR(9) NOT NULL,
        SCHOLAR_NO VARCHAR(10) NOT NULL,
        EMAIL VARCHAR(20) NOT NULL,
        MOBILE_NO CHAR(10) NOT NULL,
        ADDRESS VARCHAR(50) NOT NULL)"""

    terminal_marks_Query = """CREATE TABLE IF NOT EXISTS terminalmarks_01(
        CLASS_ID VARCHAR(4) PRIMARY KEY, 
        ENGLISH INT(3),
        EVS INT(3),
        MATHS INT(3),
        SCIENCE INT(3),
        SST INT(3),
        TOTAL INT(3),
        PERCENTAGE FLOAT(4,2),
        RANK INT(4),
        GRADE VARCHAR(2),
        STATUS VARCHAR(4)
        )"""
    
    halfyearly_marks_Query = """CREATE TABLE IF NOT EXISTS halfyearlymarks_01(
        CLASS_ID VARCHAR(4) PRIMARY KEY, 
        ENGLISH INT(3),
        EVS INT(3),
        MATHS INT(3),
        SCIENCE INT(3),
        SST INT(3),
        TOTAL INT(3),
        PERCENTAGE FLOAT(4,2),
        RANK INT(4),
        GRADE VARCHAR(2),
        STATUS VARCHAR(4)
        )"""

    annual_marks_Query = """CREATE TABLE IF NOT EXISTS annualmarks_01(
        CLASS_ID VARCHAR(4) PRIMARY KEY, 
        ENGLISH INT(3),
        EVS INT(3),
        MATHS INT(3),
        SCIENCE INT(3),
        SST INT(3),
        TOTAL INT(3),
        PERCENTAGE FLOAT(4,2),
        RANK INT(4),
        GRADE VARCHAR(2),
        STATUS VARCHAR(4)
        )"""

    teachers_details_Query = """CREATE TABLE IF NOT EXISTS techersdetails_01(
        TID INT(4) PRIMARY KEY,
        TEACHER_NAME VARCHAR(50) NOT NULL,
        FATHERS_NAME VARCHAR(50) NOT NULL,
        MOTHERS_NAME VARCHAR(50) NOT NULL,
        NO_SUBJECT_TEACHING INT(2) NOT NULL,
        DOB DATE NOT NULL,
        DOJ DATE NOT NULL,
        GENDER CHAR(1) NOT NULL,
        MARITAL_STATUS VARCHAR(3) NOT NULL,
        TRANSPORT_MODE VARCHAR(8) NOT NULL,
        ACCOUNT_NO VARCHAR(16) NOT NULL,
        AADHAR_NO VARCHARCHAR(12) NOT NULL,
        SALARY INT(5) NOT NULL,
        SALARY_PERDAY INT(4) NOT NULL,
        FREEHOLIDAYS_PERMONTH INT(1) NOT NULL,
        EMAIL VARCHAR(20) NOT NULL,
        MOBILE_NO CHAR(10) NOT NULL,
        ALTERNATE_MOBILE_NO CHAR(10) NOT NULL,
        ADDRESS VARCHAR(50) NOT NULL,
        SUBJECT_DETAILS VARCHAR(50))"""
    
    teachersal_list_Query = """CREATE TABLE IF NOT EXISTS teacherssalary_01(
        TID INT(9) PRIMARY KEY,
        APRIL INT(5) DEFAULT 0,
        APRIL_DATE DATE  DEFAULT '0000-00-00',
        APRIL_WORKINGDAYS INT(2) DEFAULT 0,
        APRIL_ATTENTEDDAYS INT(2) DEFAULT 0,
        APRIL_TOTALHOLIDAYS INT(2) DEFAULT 0,
        APRIL_ACTUALSALARY INT(5) DEFAULT 0,
        JULY INT(5) DEFAULT 0,
        JULY_DATE DATE DEFAULT '0000-00-00',
        JULY_WORKINGDAYS INT(2) DEFAULT 0,
        JULY_ATTENTEDDAYS INT(2) DEFAULT 0,
        JULY_TOTALHOLIDAYS INT(2) DEFAULT 0,
        JULY_ACTUALSALARY INT(5) DEFAULT 0,
        AUG INT(5) DEFAULT 0,
        AUG_DATE DATE DEFAULT '0000-00-00',
        AUG_WORKINGDAYS INT(2) DEFAULT 0,
        AUG_ATTENTEDDAYS INT(2) DEFAULT 0,
        AUG_TOTALHOLIDAYS INT(2) DEFAULT 0,
        AUG_ACTUALSALARY INT(5) DEFAULT 0,
        SEPT INT(5) DEFAULT 0,
        SEPT_DATE DATE DEFAULT '0000-00-00',
        SEPT_WORKINGDAYS INT(2) DEFAULT 0,
        SEPT_ATTENTEDDAYS INT(2) DEFAULT 0,
        SEPT_TOTALHOLIDAYS INT(2) DEFAULT 0,
        SEPT_ACTUALSALARY INT(5) DEFAULT 0,
        NOV INT(5) DEFAULT 0,
        NOV_DATE DATE DEFAULT '0000-00-00',
        NOV_WORKINGDAYS INT(2) DEFAULT 0,
        NOV_ATTENTEDDAYS INT(2) DEFAULT 0,
        NOV_TOTALHOLIDAYS INT(2) DEFAULT 0,
        NOV_ACTUALSALARY INT(5) DEFAULT 0,
        DEC INT(5) DEFAULT 0,
        DEC_DATE DATE  DEFAULT '0000-00-00',
        DEC_WORKINGDAYS INT(2) DEFAULT 0,
        DEC_ATTENTEDDAYS INT(2) DEFAULT 0,
        DEC_TOTALHOLIDAYS INT(2) DEFAULT 0,
        DEC_ACTUALSALARY INT(5) DEFAULT 0,
        JAN INT(5) DEFAULT 0,
        JAN_DATE DATE DEFAULT '0000-00-00',
        JAN_WORKINGDAYS INT(2) DEFAULT 0,
        JAN_ATTENTEDDAYS INT(2) DEFAULT 0,
        JAN_TOTALHOLIDAYS INT(2) DEFAULT 0,
        JAN_ACTUALSALARY INT(5) DEFAULT 0,
        FEB INT(5) DEFAULT 0,
        FEB_DATE DATE DEFAULT '0000-00-00',
        FEB_WORKINGDAYS INT(2) DEFAULT 0,
        FEB_ATTENTEDDAYS INT(2) DEFAULT 0,
        FEB_TOTALHOLIDAYS INT(2) DEFAULT 0,
        FEB_ACTUALSALARY INT(5) DEFAULT 0,
        MARCH INT(5) DEFAULT 0, 
        MARCH_DATE DATE DEFAULT '0000-00-00',
        MARCH_WORKINGDAYS INT(2) DEFAULT 0,
        MARCH_ATTENTEDDAYS INT(2) DEFAULT 0,
        MARCH_TOTALHOLIDAYS INT(2) DEFAULT 0,
        MARCH_ACTUALSALARY INT(5) DEFAULT 0,
        TRANSPORT_FEES INT(4) DEFAULT 0,
        ANNUAL_SALARY INT(5) DEFAULT 0,
        TOTAL_PAID INT(5) DEFAULT 0,
        SALARY_DUE INT(5) DEFAULT 0,
        FOREIGN KEY(TID) REFERENCES  techersdetails_01(TID)
        )"""

    schoolexpanse_Query = """CREATE TABLE IF NOT EXISTS schoolexpense_01(
        EXPANSE_NAME VARCHAR(10), 
        AMOUNT INT(5),
        DATE DATE NOT NULL,
        MONTH VARCHAR(10))"""

    newuser_Query = """CREATE TABLE IF NOT EXISTS newuser_01(
        USERID VARCHAR(10) PRIMARY KEY NOT NULL, 
        PASSWORD VARCHAR(70) NOT NULL,
        NAME VARCHAR(50) NOT NULL,
        CLASS VARCHAR(5))"""

    students_attendance_Query = """CREATE TABLE IF NOT EXISTS stuattendance_01(
        CLASS_ID VARCHAR(4) PRIMARY KEY,
        APRIL INT(5) DEFAULT 0,
        APRIL_WORKINGDAYS INT(2) DEFAULT 0,
        APRIL_ATTENTEDDAYS INT(2) DEFAULT 0,
        APRIL_TOTALHOLIDAYS INT(2) DEFAULT 0,
        JULY INT(5) DEFAULT 0,
        JULY_WORKINGDAYS INT(2) DEFAULT 0,
        JULY_ATTENTEDDAYS INT(2) DEFAULT 0,
        JULY_TOTALHOLIDAYS INT(2) DEFAULT 0,
        AUG INT(5) DEFAULT 0,
        AUG_WORKINGDAYS INT(2) DEFAULT 0,
        AUG_ATTENTEDDAYS INT(2) DEFAULT 0,
        AUG_TOTALHOLIDAYS INT(2) DEFAULT 0,
        SEPT INT(5) DEFAULT 0,
        SEPT_WORKINGDAYS INT(2) DEFAULT 0,
        SEPT_ATTENTEDDAYS INT(2) DEFAULT 0,
        SEPT_TOTALHOLIDAYS INT(2) DEFAULT 0,
        NOV INT(5) DEFAULT 0,
        NOV_WORKINGDAYS INT(2) DEFAULT 0,
        NOV_ATTENTEDDAYS INT(2) DEFAULT 0,
        NOV_TOTALHOLIDAYS INT(2) DEFAULT 0,
        DEC INT(5) DEFAULT 0,
        DEC_WORKINGDAYS INT(2) DEFAULT 0,
        DEC_ATTENTEDDAYS INT(2) DEFAULT 0,
        DEC_TOTALHOLIDAYS INT(2) DEFAULT 0,
        JAN INT(5) DEFAULT 0,
        JAN_WORKINGDAYS INT(2) DEFAULT 0,
        JAN_ATTENTEDDAYS INT(2) DEFAULT 0,
        JAN_TOTALHOLIDAYS INT(2) DEFAULT 0,
        FEB INT(5) DEFAULT 0,
        FEB_WORKINGDAYS INT(2) DEFAULT 0,
        FEB_ATTENTEDDAYS INT(2) DEFAULT 0,
        FEB_TOTALHOLIDAYS INT(2) DEFAULT 0,
        MARCH INT(5) DEFAULT 0, 
        MARCH_WORKINGDAYS INT(2) DEFAULT 0,
        MARCH_ATTENTEDDAYS INT(2) DEFAULT 0,
        MARCH_TOTALHOLIDAYS INT(2) DEFAULT 0)"""
    
    

    cursor.execute(student_details_Query)
    cursor.execute(students_fees_Query)
    cursor.execute(fees_list_Query)
    cursor.execute(transport_list_Query)
    cursor.execute(backup_data_Query)
    cursor.execute(terminal_marks_Query)
    cursor.execute(halfyearly_marks_Query)
    cursor.execute(annual_marks_Query)
    cursor.execute(teachers_details_Query)
    cursor.execute(teachersal_list_Query)
    cursor.execute(schoolexpanse_Query)
    cursor.execute(newuser_Query)
    cursor.execute(students_attendance_Query)






    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")
