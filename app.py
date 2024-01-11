from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectField
from wtforms.validators import DataRequired
import pyodbc
import sys
import os
sys.path.insert(0, os.path.abspath('classes'))
import users
from course import Course_class
from Students import students
from Teacher import teacher
from Upload import upload
from submissions import submissions



app = Flask(__name__)
app.secret_key = 'super_secret_key'



class SignInForm(FlaskForm):
    Email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
    Email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    type = SelectField(u'Type',choices=['Student', 'Teacher','Supervisor'], validators=[DataRequired()])
    submit = SubmitField('Sign Up')

@app.route('/')
def index():
    return render_template('index.html')


main_user=users.users()

@app.route('/create_course', methods=['POST'])
def create_course():
    course_name = request.form['course_name']
    teacher_name = request.form['teacher_name']
    year = request.form['year']
    semester = request.form['semester']
    course_capacity = request.form['course_capacity']
    course=Course_class(course_name,year,semester,course_capacity,teacher_name)
    found=course.createCourse()
    if found:
        flash('Course created successfully!', 'success')
        return redirect(url_for('home'))
    else:
        return "error please revise your input"


@app.route('/Create_upload', methods=['POST'])
def create_announcement():
    request_data = request.form
    Course_code = request_data['CourseCode']
    Upload_type = request_data['Type']
    Upload_title = request_data['Title']
    Upload_Description = request_data['Description']
    Upload_link = request_data['Link']
    




    # Create a new announcement.
    Upload = upload()
    Upload.insert_upload(Upload_title,Upload_type,Upload_Description, Upload_link,Course_code)
    if Upload_type=="Assignment":
        A_deadline = request_data['deadline']
        A_grade= request_data['assigngrade']
        while A_grade == "None":
            flash('Please enter grade', 'error')
        submission=submissions()
        submission.createSubmission(Upload.id,Course_code,A_grade,A_deadline)
    return redirect(url_for('courses'))

@app.route('/Signin', methods=['GET', 'POST'])
def sign_in():
    form = SignInForm()

    if form.validate_on_submit():
        Email = form.Email.data
        password = form.password.data
        user=users.users()
        user.sign_in_values(Email,password)
        found=user.sign_in_validation()
        if found:
            First_name,Last_name,id,send_type=user.sign_in_get_data()
            name=First_name+" "+Last_name
            main_user.get_main(name,send_type,user.email,id)
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('Signin.html', form=form)

@app.route('/enroll_course', methods=['POST'])
def enroll():
    course_id = request.form['course_id']
    student_user=students(main_user.id)
    found=student_user.addStudentToCourse(course_id)
    if not found:
        return "error please revise your input"
    else:
        flash('Course enrolled successfully!', 'success')
        return redirect(url_for('home'))


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()

    if form.validate_on_submit():
        Email = form.Email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        type = form.type.data
        user=users.users()
        user.sign_up_values(Email,password,first_name,last_name,type)
        user.sign_up()
        flash(f'Email: {Email}, Password: {password} created successfully!', 'success')
        return redirect(url_for('sign_in'))
    return render_template('signup.html', form=form)

@app.route('/home')
def home():
    name = main_user.name
    id = main_user.id
    type = main_user.type
    email=main_user.email
    teacher_user=teacher(main_user.id)
    course_codes,course_names=teacher_user.get_courses_info()
    course_students=teacher_user.get_students_in_course()

    return render_template('home.html',name=name,id=id, type=type,email=email,course_codes=course_codes,course_names=course_names,course_students=course_students)

# @app.route('/layout')
# def layout():
#     name = request.args.get('name')
#     id = request.args.get('id')
#     send_type = request.args.get('send_type')
#     return render_template('Layout.html',name=name,id=id,send_type=send_type)


@app.route('/courses',methods=['GET','POST'])
def courses():
    if main_user.type=="Student":
        type_user=students(main_user.id)
    elif main_user.type=="Teacher":
        type_user=teacher(main_user.id)
    course_codes=type_user.get_courses()
    upload_id=[]
    upload_header=[]
    upload_type=[]
    upload_description=[]
    upload_link=[]
    upload_date=[]
    for i in course_codes:
        upload_it=upload()
        upload_it.upload_info(i)
        upload_list=[]
        header_list=[]
        type_list=[]
        description_list=[]
        link_list=[]
        date_list=[]

        for j in range(len(upload_it.up_id)):
            upload_list.append(upload_it.up_id[j])
            header_list.append(upload_it.up_header[j])
            type_list.append(upload_it.up_type[j])
            description_list.append(upload_it.up_desc[j])
            link_list.append(upload_it.up_link[j])
            date_list.append(upload_it.up_date[j])

        upload_description.append(description_list)        
        upload_id.append(upload_list)
        upload_header.append(header_list)
        upload_type.append(type_list)
        upload_link.append(link_list)
        upload_date.append(date_list)

    courses=course_codes
    if courses:
        return render_template('courses.html',courses=course_codes,upload_id=upload_id,upload_header=upload_header,upload_type=upload_type,user_type=main_user.type,upload_description=upload_description,upload_date=upload_date,upload_link=upload_link)
    else:
        return "error please revise your input"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
       app.run(host="0.0.0.0",port=80,debug=True)
