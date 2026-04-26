class student:
    name=input('Please enter your name :')
    collage = input("please enter your collage name :")
    age=int(input("please enter your age :"))

# create object
stu1 = student()
stu2 = student()

#object calling
print(f"Student's name : {stu1.name} \nStudent's collage : {stu1.collage}\n Student's age : {stu1.age}")