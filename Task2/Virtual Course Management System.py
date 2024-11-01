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
    


