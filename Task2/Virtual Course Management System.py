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
class Student_t:

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = str(grade)

    def introduce(self):
        return '{} {} {}'.format(self.name, self.age, self.subject)

#create a basic course.    
class Course_t:

    def __init__(self, course_name, teacher, students=None):
        self.course_name = str(course_name)
        self.teacher = Teacher_t(teacher)
        if students is None:
            self.students = []
        else:
            self.students = students
    
    def add_student(self, stud):
        if stud not in self.students:
            self.students.append(stud)

    def remove_student(self, stud):
        if stud in self.students:
            self.students.remove(stud)

    def show_course_info(self):
        for stud in self.students:
            print(self.course_name, self.teacher, self.students)

#teach_1 = Teacher_t('LiHua', 18, 'Math')
#teach_2 = Teacher_t('WangYang', 89, 'Chinese')

#stud_1 = Student_t('Dlan', 20, 'freshman')
#stud_2 = Student_t('Daniel', 21, 'sophomore')
#stud_3 = Student_t('Dlancy', 22 ,'junior')
