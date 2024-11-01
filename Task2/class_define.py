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

