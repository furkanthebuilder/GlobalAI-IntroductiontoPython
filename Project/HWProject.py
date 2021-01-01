#Simple Stuent Management System
#Single student enter name-surname
#Student can enter 3 wrong answers before system goes off
#After entering student can take min 3 max 5 courses
#If student take less than 3 classes he fails
#Then student should choise 1 couce to take exam. The student notes are predifned in dictionary
#Dictionary should contain midter, final, projcect
#Then the system will determine the grades

import math

from StudentInfo import StudentName 
from StudentInfo import StudentSurname
from StudentInfo import Courses
from StudentInfo import Grades as gr



def askidentification():
    
    check = int(3)
    while check >= 0:
        user_name = input('User_Name = ').upper()
        user_surname = input('User_Surname = ').upper()
        if user_name in StudentName and user_surname in StudentSurname and check >= 0:

            print("Welcome")
            identification = True
            break
            

        elif user_name not in StudentName and user_surname not in StudentSurname and check > 0:

            print("Unidentified Name")
            print("Unidentified Surname")
            check = check - 1
            print("Checks left= ", check)


        elif user_name in StudentName and user_surname not in StudentSurname and check > 0:

            print("Unidentified Surname")
            check = check -1
            print("Checks left= ", check)


        elif user_name not in StudentName and user_surname in StudentSurname and check > 0:

            print("Unidentified Name")
            check = check -1
            print("Checks left= ", check)


        else:
            print("Unidentified")
            print("Please try again later")
            identification = False
            break
            

    if identification:
        return True
    else:
        return False

def courseregistration():

    count = 1
    stop = False
    while count < 6 and not stop :

        cont = input('Enter course name = ').upper()
        print("Enter -STOP- to end process")


        if cont == "STOP":
            stop = True


        else:
            course_name = cont
            Courses.append(course_name)
            print("Added course = ", course_name)
            print("Number of added cources {}".format(count))
            count = count + 1
        
    if count < 3:
        return False
    else:
        print("Numver of added courses {}".format(count))
        print("Registered cources = ", Courses)
        return True


def exampicking():
    x = True
        
    while x:
        picked = input("Pick a course from added cources = ").upper()
        print("Added cources ", Courses)

        if picked in Courses:
            print("Valid input")
            x = False
            return picked

        else:
            print("This course is not added \n Please try again ")


def Lettergrade(Totalscore):

    if Totalscore < 30:
        print("Letter Grade = FF")
        print("You failed this course")
    elif 30 <= Totalscore and Totalscore < 50:
        print("Letter Grade = DD")
    elif 50 <= Totalscore and Totalscore < 70:
        print("Letter Grade = CC")
    elif 70 <= Totalscore and Totalscore < 90:
        print("Letter Grade = BB")             
    elif 90 <= Totalscore:
        print("Letter Grade = AA")






if __name__ == "__main__":
    Idsystemworks = True   
    Registration = True
    examselection = True
    
# For demo user name: user surname: guest
# Saved cources names are DERS1,DERS2,DERS3,DERS4,DERS5 use these names to add courses
# Saved files are in Studentşnfo.py

    # Student Id system
    # Checks initials of the user with Studentinfo.py list
    while Idsystemworks:
        studentidcheck = askidentification()
        if studentidcheck:
            print("Studdet Identified")
            Idsystemworks = False
        else:
            print("Student Couldn't be Identified")
            Idsystemworks = False


    # Course registration system
    # Takes user input cources then adds them into a list
    while Registration:
        registrationcheck =  courseregistration()
        if registrationcheck:
            print("Registration complete")
            Registration = False
        else:
            print("You failed the class")
            Registration = False
            break

    
    # Exam selection system
    # Student pick one cource from registered cources then check the grade from courcegrades
    while examselection:
        exam = exampicking()
        print("Selected exam is = ", exam)
        
        for i in range(0,5):
            if exam == gr[i]['Course']:
                save = i
                print(" Midterm Grade = ", gr[save]['midterm'], "\n",
                      "Final Grade = ", gr[save]['final'], "\n",
                      "Project Grade = ", gr[save]['project'])

        examselection = False
    
    #Grading Process
    Midtermexam = gr[save]['midterm'] * 30 / 100
    Finalexam = gr[save]['final'] * 50 / 100
    Projectexam = gr[save]['project'] * 20 / 100
    Totalscore = Midtermexam + Finalexam + Projectexam
    print("Total Score = ", Totalscore)

    Lettergrade(Totalscore)



    

        

    



    



    
