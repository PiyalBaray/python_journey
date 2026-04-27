# How to create a methods(function) in constructor
class collage :
    def __init__(self,student_name,student_class):
        self.student_name = student_name
        self.student_class = student_class

    # create a method
    def student(self):
        return self.student_class

# create object
stu1 = collage("piyal","2nd year")

#print
print(f"My name is {stu1.student_name} i am student of {stu1.student()} ")