#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grade - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:

    # properties should be listed first
    name = ''
    studentNumber = ''
    grade=0
    courses=[]
    grades=[]

    def __init__(self,name,studentNumber,grade,courses=[],grades=[]): # You will need to create your own input parameters for all methods
        self.name = name
        self.studentNumber = studentNumber
        self.grade = grade
        self.courses = courses
        self.grades = grades

    def __del__(self):
        print("Thank you for viewing the profile of " +self.name +'.')

    def average(self,grades):
        length=len(grades)
        num2=0
        for i in range(0,length):
            num1=grades[i]
            num2=num2+num1
        return num2
    def getHonorRoll(self):
        lis=self.grades
        length=len(lis)
        if length<5:
            ans=print('Student does not have enough courses.')
            return ans
        else: 
            lis.sort()
            average=(lis[-1]+lis[-2]+lis[-3]+lis[-4]+lis[-5])/5
            return average
    def showCourses(self):
        lis=self.courses
        ans=print(lis)
        return ans
    def showGrade(self,ind):
        class1=self.courses
        course=class1[ind]
        grades=self.grades
        grades2=grades[ind]
        ans=print(self.name+' has a '+ str(grades2) + '%'+' in the course' + str(course)+'.')
        return ans
    def getCourses(self,lis1):
        
        self.courses=lis1
        
    def getGrades(self,grade1,grade2,grade3,grade4,grade5,grade6,grade7):
        lis1=[]
        lis1.insert(grade1,0)
        lis1.insert(grade2,1)
        lis1.insert(grade3,2)
        lis1.insert(grade4,3)
        lis1.insert(grade5,4)
        lis1.insert(grade6,5)
        lis1.insert(grade7,6)
        
        self.grades=lis1
        
        
        




def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( 91, 94, 87, 99, 82, 100, 73)

    st2 = student("Joe Lunchbox","12346", 11)
    st1.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st1.getGrades( 71, 98, 93, 95, 68, 81, 71)




main()