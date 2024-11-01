#Python Objected-Oriented Programming
#实现虚拟课程管理系统
#@file class_define.py
#@brief class_instnce/实例化并调用函数
#@author Yc-Dlan
#@version 1.0
#@date 2024.11.1
#@note 实例化了各种类，并调用了各种函数，查看代码的可行性

#创建Person_t的基类/create a basic person class.
class Person_t:
    
    #定义变量name和age
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)

    #定义introduce函数，用于输出信息/define function_introduce for print basic information
    def introduce(self):
        return '{} {}'.format(self.name, self.age)

#继承Person_t创建Teacher_t类/create a subclass_teacher
class Teacher_t(Person_t):
    
    def __init__(self, name, age, subject):

        #继承name和age，并创建新变量subject
        super().__init__(name, age)
        self.subject = str(subject)

    #重写introduce函数
    def introduce(self):
        return '{} {} {}'.format(self.name, self.age, self.subject)
    
#继承Person_t创建Student_t类/create a subclass_student
class Student_t(Person_t):

    def __init__(self, name, age, grade):
        #继承并创建新的变量grade
        super().__init__(name, age)
        self.grade = str(grade)

    #重写introduce函数
    def introduce(self):
        return '{} {} {}'.format(self.name, self.age, self.grade)

#创建新的基类Course_t/create a basic course.    
class Course_t:

    #定义基本变量course_name，teacher和student列表
    def __init__(self, course_name, teacher=None, students=None):
        self.course_name = str(course_name)
        self.teacher = teacher

        #为列表赋初值
        if students is None:
            self.students = []
        else:
            self.students = students
    
    #定义添加学生信息的add函数/define function_add to add new student information
    def add_student(self, stud):
        if stud not in self.students:
            self.students.append(stud)

    #定义删除学生信息的remove函数/define function_remove to remove the student's information
    def remove_student(self, stud):
        if stud in self.students:
            self.students.remove(stud)

    #定义输出相关信息的show函数/define function_show_course_info for print course information
    def show_course_info(self):
        print(f"课程名称：{self.course_name}")
        print(f"授课教师：{self.teacher.name}, 教授科目：{self.teacher.subject}")
        print("选修学生列表：")
        for student in self.students:
            print(student.introduce())

#构建两个教师实例/create teacher_instantiation             
teach_1 = Teacher_t('LiHua', 47, 'Math')
teach_2 = Teacher_t('WangYang', 57, 'Chinese')

#构建三个学生实例/create student_instantiation
stud_1 = Student_t('Dlan', 20, 'freshman')
stud_2 = Student_t('Daniel', 21, 'sophomore')
stud_3 = Student_t('Dlancy', 22 ,'junior')

#构建两个课程实例/create course_instantiation
cour_1 = Course_t('Math')
cour_2 = Course_t('Chinese')

#分配教师属性/distribute teacher attribute
cour_1.teacher = teach_1
cour_2.teacher = teach_2

#调用add_student函数/add 3 new students in the courses' list
cour_1.add_student(stud_1)
cour_1.add_student(stud_2)
cour_2.add_student(stud_3)

#调用show_course_info()函数/showcase the course information
print('--->showcase the course information after the add_function:')
cour_1.show_course_info()
cour_2.show_course_info()
print('\n')

#调用remove函数/remove stud_1 from the course information
cour_1.remove_student(stud_1)

#再次展示/showcase the course information after the remove_function
print('--->showcase the course information after the remove_function:')
cour_1.show_course_info()