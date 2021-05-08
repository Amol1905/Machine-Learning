import pandas as pd
import numpy as np
import os.path
class Details:
    def __init__(self):
        self.ID = None
        self.NAME = None
        self.COLLEGE_NAME = None
        self.DEPARTMENT_NAME = None
        self.ADDRESS = None
        self.PHONE = None
        self.EMAIL = None
    def setData(self,ID,NAME,COLLEGE_NAME,DEPARTMENT_NAME,ADDRESS,PHONE,EMAIL):
        self.ID = ID
        self.NAME = NAME
        self.COLLEGE_NAME =COLLEGE_NAME
        self.DEPARTMENT_NAME = DEPARTMENT_NAME
        self.ADDRESS = ADDRESS
        self.PHONE = PHONE
        self.EMAIL = EMAIL

class Student(Details):
    studentDataFrame = None
    def __init__(self):
        super().__init__()  
        self.DOB = None
        self.SData = None
    
    def setStudentData(self,ID,NAME,COLLEGE_NAME,DEPARTMENT_NAME,ADDRESS,PHONE,EMAIL,DOB):
        self.setData(ID,NAME,COLLEGE_NAME,DEPARTMENT_NAME,ADDRESS,PHONE,EMAIL) 
        self.DOB = DOB
        self.SData = {
            'ID':self.ID,
            'NAME':self.NAME,
            'DOB':self.DOB,
            'COLLEGE_NAME':self.COLLEGE_NAME,
            'DEPARTMENT_NAME': self.DEPARTMENT_NAME,
            'ADDRESS':self.ADDRESS,
            'PHONE':self.PHONE,
            'EMAIL':self.EMAIL
        }
        # Student.studentDataFrame = pd.DataFrame(self.SData)
        Student.studentDataFrame = pd.DataFrame(self.SData,index = [self.ID])
        if os.path.isfile('Student_Data.csv'):
            with open("Student_Data.csv",'a',) as f:
                Student.studentDataFrame.to_csv(f,header = False,index = None)
        else:
            with open("Student_Data.csv",'a',) as f:
                Student.studentDataFrame.to_csv(f,index = None)

    def displayStudentData(self):
        with open("Student_Data.csv",'r') as f:
            self.showData = pd.read_csv(f)
            print(self.showData)
class Teacher(Details):
    teacherDataFrame = None
    def __init__(self):
        super().__init__()  
        self.SALARY = None
        self.TData = None

    def setTeacherData(self,ID,NAME,COLLEGE_NAME,DEPARTMENT_NAME,ADDRESS,PHONE,EMAIL,SALARY):
        self.setData(ID,NAME,COLLEGE_NAME,DEPARTMENT_NAME,ADDRESS,PHONE,EMAIL) 
        self.SALARY = SALARY 
        self.TData = {
            'ID':self.ID,
            'NAME':self.NAME,
            'SALARY':self.SALARY,
            'COLLEGE_NAME':self.COLLEGE_NAME,
            'DEPARTMENT_NAME': self.DEPARTMENT_NAME,
            'ADDRESS':self.ADDRESS,
            'PHONE':self.PHONE,
            'EMAIL':self.EMAIL
        }
        # Student.studentDataFrame = pd.DataFrame(self.SData)
        Teacher.teacherDataFrame = pd.DataFrame(self.TData,index = [self.ID])
        if os.path.isfile('Teacher_Data.csv'):
            with open("Teacher_Data.csv",'a',) as f:
                Teacher.teacherDataFrame.to_csv(f,header = False,index = None)
        else:
            with open("Teacher_Data.csv",'a',) as f:
                Teacher.teacherDataFrame.to_csv(f,index = None)

    def displayTeacherData(self):
        with open("Teacher_Data.csv",'r') as f:
            self.showData = pd.read_csv(f)
            print(self.showData)
    
class Menu(Student,Teacher):
    def Options(self):
        ch = 0
        s = Student()
        t = Teacher()
        print("1.Add Data\n2.Update\n3.Show Data\n4.Delete Data\n5.To Exit")
        ch = int(input("Enter Your Choice: "))
        while ch < 5:
            if ch == 1:
                ch1 = 0
                print("In Which Database Do you want to add ?\n1.Student Data\n2.Teacher Data")
                ch1 = int(input("Enter Your Choice: "))
                while ch1 < 3:
                    if ch1 == 1:
                        self.ID = int(input("ENTER STUDENT ID: "))
                        self.NAME = input("ENTER STUDENT NAME: ")
                        self.DOB = input("ENTER STUDENT DATE OF BIRTH: ")
                        self.COLLEGE_NAME = input("ENTER STUDENT COLLEGE NAME: ")
                        self.DEPARTMENT_NAME = input("ENTER STUDENT DEPARTMENT NAME: ")
                        self.ADDRESS = input("ENTER STUDENT ADDRESS: ")
                        self.PHONE = int(input("ENTER STUDENT PHONE: "))
                        self.EMAIL = input("ENTER STUDENT EMAIL: ")
                        s.setStudentData(self.ID,self.NAME,self.COLLEGE_NAME,self.DEPARTMENT_NAME,self.ADDRESS,self.PHONE,self.EMAIL,self.DOB)
                        print("1.Add More In Student ?\n3.To Main Menu")
                        ch1 = int(input("Enter Your Choice: "))
                    elif ch1 == 2:
                        self.ID = int(input("ENTER TEACHER ID: "))
                        self.NAME = input("ENTER TEACHER NAME: ")
                        self.SALARY = input("ENTER SALARY OF TEACHER : ")
                        self.COLLEGE_NAME = input("ENTER TEACHER COLLEGE NAME: ")
                        self.DEPARTMENT_NAME = input("ENTER TEACHER DEPARTMENT NAME: ")
                        self.ADDRESS = input("ENTER TEACHER ADDRESS: ")
                        self.PHONE = int(input("ENTER TEACHER PHONE: "))
                        self.EMAIL = input("ENTER TEACHER EMAIL: ")
                        t.setTeacherData(self.ID,self.NAME,self.COLLEGE_NAME,self.DEPARTMENT_NAME,self.ADDRESS,self.PHONE,self.EMAIL,self.SALARY)
                        print("2.Add More In Teacher ?\n3.To Main Menu")
                        ch1 = int(input("Enter Your Choice: "))
            elif ch == 2:
                print("Which Data do you want to Update\n1.Student Data\n2.Teacher Data")
                ch2 = int(input("Enter your Choice: "))
                while ch2 < 3:
                    if ch2 == 1:
                        st = pd.read_csv('Student_Data.csv')
                        st.set_index('ID',inplace = True)
                        print("Before Update ...............")
                        print(st)
                        index = int(input("ENTER ID OF STUDENT TO UPDATE: "))
                        column,value = input(f"ENTET COLUMN NAME AND VALUE TO CHANGE VALUE AT {index} : ").split(" ")
                        st.loc[index,column] = value
                        st.to_csv('Student_Data.csv')
                        print("After Update ...............")
                        print(st)
                        print("1.Update More In Student ?\n3.To Main Menu")
                        ch2 = int(input("Enter Your Choice: "))

                    elif ch2 == 2:
                        st = pd.read_csv('Teacher_Data.csv')
                        st.set_index('ID',inplace = True)
                        print("Before Update ...............")
                        print(st)
                        index = int(input("ENTER ID OF TEACHER TO UPDATE: "))
                        column,value = input(f"ENTET COLUMN NAME AND VALUE TO CHANGE VALUE AT {index} : ").split(" ")
                        st.loc[index,column] = value
                        st.to_csv('Teacher_Data.csv')
                        print("After Update ...............")
                        print(st)
                        print("2.Update More In Teacher ?\n3.To Main Menu")
                        ch2 = int(input("Enter Your Choice: "))

            elif ch == 3:
                print("Which Data do you want to show\n1.Student Data\n2.Teacher Data")
                ch3 = int(input("Enter your Choice: "))
                if ch3 == 1:
                    s.displayStudentData()
                elif ch3 ==2:
                    t.displayTeacherData()
            elif ch == 4:
                print("Which Data do you want to Delete\n1.Student Data\n2.Teacher Data")
                ch4 = int(input("Enter your Choice: "))
                while ch4 < 3:
                    if ch4 == 1:
                        st = pd.read_csv('Student_Data.csv')
                        st.set_index('ID',inplace = True)
                        print("Before Delete ...............")
                        print(st)
                        index = int(input("ENTER ID OF STUDENT TO DELETE: "))
                        st.drop([index],axis = 0,inplace = True)
                        st.to_csv('Student_Data.csv')
                        print("After Delete ...............")
                        print(st)
                        print("1.Delete More In Student ?\n3.To Main Menu")
                        ch4 = int(input("Enter Your Choice: "))

                    elif ch4 == 2:
                        st = pd.read_csv('Teacher_Data.csv')
                        st.set_index('ID',inplace = True)
                        print("Before Delete ...............")
                        print(st)
                        index = int(input("ENTER ID OF TEACHER TO DELETE: "))
                        st.drop([index],axis = 0,inplace = True)
                        st.to_csv('Teacher_Data.csv')
                        print("After Delete ...............")
                        print(st)
                        print("2.Delete More In Teacher ?\n3.To Main Menu")
                        ch4 = int(input("Enter Your Choice: "))

            print("Do you want to continue.... ?")
            con = int(input("Enter Your Choice (1/0): "))
            if con == 1:
                print("1.Add Data\n2.Update\n3.Show Data\n4.Delete Data\n5.To Exit")
                ch = int(input("Enter Your Choice: "))
            else:
                ch = 5

m = Menu()
m.Options()

# t = pd.read_csv("Teacher_Data.csv")
# t.set_index('ID',inplace = True)
# # t.drop(t.iloc[12,])
# t.drop([12],axis = 0,inplace = True)
# t.to_csv("Teacher_Data.csv")
# print(t)


