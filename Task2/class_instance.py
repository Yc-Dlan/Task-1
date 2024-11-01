#Python Objected-Oriented Programming
#实现虚拟课程管理系统

#create a basic person class.
class Person_t:
    
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)

    #define function_introduce for print basic information
    def introduce(self):
        return '{} {}'.format(self.name, self.age)

#create a subclass_teacher
class Teacher_t(Person_t):
    
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = str(subject)

    def introduce(self):
        return '{} {} {}'.format(self.name, self.age, self.subject)
    
#create a subclass_student
class Student_t(Person_t):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = str(grade)

    def introduce(self):
        return '{} {} {}'.format(self.name, self.age, self.grade)

#create a basic course.    
class Course_t:

    def __init__(self, course_name, teacher=None, students=None):
        self.course_name = str(course_name)
        
        self.teacher = teacher
            
        if students is None:
            self.students = []
        else:
            self.students = students

    #define function_add to add new student information
    def add_student(self, stud):
        if stud not in self.students:
            self.students.append(stud)

    #define function_remove to remove the student's information
    def remove_student(self, stud):
        if stud in self.students:
            self.students.remove(stud)

    #define function_show_course_info for print course information
    def show_course_info(self):
        print(f"课程名称：{self.course_name}")
        print(f"授课教师：{self.teacher.name}, 教授科目：{self.teacher.subject}")
        print("选修学生列表：")
        for student in self.students:
            print(student.introduce())

#create teacher_instantiation             
teach_1 = Teacher_t('LiHua', 47, 'Math')
teach_2 = Teacher_t('WangYang', 57, 'Chinese')

#create student_instantiation
stud_1 = Student_t('Dlan', 20, 'freshman')
stud_2 = Student_t('Daniel', 21, 'sophomore')
stud_3 = Student_t('Dlancy', 22 ,'junior')

#create course_instantiation
cour_1 = Course_t('Math')
cour_2 = Course_t('Chinese')

#distribute teacher attribute
cour_1.teacher = teach_1
cour_2.teacher = teach_2

#add 3 new students in the courses' list
cour_1.add_student(stud_1)
cour_1.add_student(stud_2)
cour_2.add_student(stud_3)

#showcase the course information
print('--->showcase the course information after the add_function:')
cour_1.show_course_info()
cour_2.show_course_info()
print('\n')

#remove stud_1 from the course information
cour_1.remove_student(stud_1)

#showcase the course information after the remove_function
print('--->showcase the course information after the remove_function:')
cour_1.show_course_info()