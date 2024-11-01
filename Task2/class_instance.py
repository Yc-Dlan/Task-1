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
    
    def add_student(self, stud):
        if stud not in self.students:
            self.students.append(stud)

    def remove_student(self, stud):
        if stud in self.students:
            self.students.remove(stud)

    def show_course_info(self):
        print(f"课程名称：{self.course_name}")
        print(f"授课教师：{self.teacher.name}, 教授科目：{self.teacher.subject}")
        print("选修学生列表：")
        for student in self.students:
            student.introduce()

teach_1 = Teacher_t('LiHua', 47, 'Math')
teach_2 = Teacher_t('WangYang', 57, 'Chinese')

stud_1 = Student_t('Dlan', 20, 'freshman')
stud_2 = Student_t('Daniel', 21, 'sophomore')
stud_3 = Student_t('Dlancy', 22 ,'junior')

cour_1 = Course_t('Math')
cour_2 = Course_t('Chinese')

cour_1.teacher = teach_1
cour_2.teacher = teach_2

# 添加学生前检查
print("添加学生前，cour_1的学生列表：")
print(cour_1.students)  # 应该显示 []

# 添加学生
cour_1.add_student(stud_1)
cour_1.add_student(stud_2)
cour_1.add_student(stud_3)

# 添加学生后检查
print("\n添加学生后，cour_1的学生列表：")
print(cour_1.students)  # 应该显示 [stud_1, stud_2]

# 打印课程信息
print("\n使用show_course_info方法打印cour_1的课程信息：")
cour_1.show_course_info()

# 尝试重复添加同一个学生
cour_1.add_student(stud_1)  # 这应该不会改变学生列表

# 再次检查学生列表，确认没有重复添加
print("\n尝试重复添加后，cour_1的学生列表：")
print(cour_1.students)  # 应该仍然显示 [stud_1, stud_2]

# 打印课程信息，确认学生列表正确
print("\n再次使用show_course_info方法打印cour_1的课程信息：")
cour_1.show_course_info()