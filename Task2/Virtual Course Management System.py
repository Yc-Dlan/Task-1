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

#create a basic course.    
class Course_t:

    def __init__(self, course_name, teacher, student):
        pass

per_1 = Person_t('LiHua', 18)
per_2 = Person_t('WangYang', 89)


print(Person_t.introduce(per_1))
print(Person_t.introduce(per_2))