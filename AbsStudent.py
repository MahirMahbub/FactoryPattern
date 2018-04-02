class AbsStudent( object ):
    def __init__(self, roll, name):
        self._roll = roll
        self._name = name

    def myDetsils(self):
        self.printNameANDRoll()
        self.printOtherDetails()

    def printOtherDetails(self):
        pass

    def printNameANDRoll(self):
        print( "I am " + str(self._name ))
        print( "My roll is " + str(self._roll) )


class ICourse( object ):
    def printCourseDetails(self):
        pass

    def addStudent(self, student):
        pass

    def addTeacher(self, teacher):
        pass


class ITeacher( object ):
    def teacherDetails(self):
        pass


class AbsTeacher( ITeacher ):

    def __init__(self, name):
        self._name = name

    def teacherDetails(self):
        print( "I am " + self._name )
        self.otherDetails()

    def otherDetails(self):
        pass


class Factory( object ):

    def __init__(self):
        self.bulitCourse()
        self.addStudentsToCourse()
        self.addTeacherToCourse()

    def bulitCourse(self):
        pass

    def addStudentsToCourse(self):
        pass

    def addTeacherToCourse(self):
        pass

    def viewCOurseInformation(self):
        self.course.printCourseDetailse()

    def getCourse(self):
        return self.course


class FactoryOFFactory( object ):

    def __init__(self):
        self.factoryMap = {}
        self.init()

    def init(self):
        self.factoryMap[503] = BusinessCommunicationFactory()
        self.factoryMap[504] = DBMS2Factory()

    def getFactory(self, courseNumber):
        return self.factoryMap[courseNumber]


class Course( ICourse ):
    def __init__(self, courseName):
        self.courseName = courseName
        self.allStudent = []
        self.allTeacher = []

    def printCourseDetails(self):
        print( "---------------------------------------" )
        print( "course name:: " + self.courseName )
        print()
        for student in self.allStudent:
            student.myDetsils()
        print()
        for teacher in self.allTeacher:
            teacher.teacherDetails()
            print()
            print( "---------------------------------------" )

    def addStudent(self,student):
        self.allStudent.append( student )

    def addTeacher(self, teacher):
        self.allTeacher.append( teacher )

class BusinessCommunicationTeacher( AbsTeacher ):

    def BusinessCommunicationStudent(self, name):
        super( name )

    def printOtherDetails(self):
        print( "I teach business communication." )


class BusinessCommunicationStudent( AbsStudent ):

    def BusinessCommunicationStudent(self, roll, name):
        super( roll, name )

    def printOtherDetails(self):
        print( "This is my one of the favourite course. Teacher teach us few time in this course." )


class BusinessCommunicationFactory( Factory ):

    def bulitCourse(self):
        self.course = Course( "Business communication - 503" )

    def addStudentsToCourse(self):
        self.course.addStudent( BusinessCommunicationStudent( 816, "Imam Hossain Kawser" ) )
        self.course.addStudent( BusinessCommunicationStudent( 817, "Atiq Ahammed" ) )
        self.course.addStudent( BusinessCommunicationStudent( 818, "Hasan Tarek" ) )
        self.course.addStudent( BusinessCommunicationStudent( 819, "Chinmoy Achaerjee" ) )

    def addTeacherToCourse(self):
        self.course.addTeacher( BusinessCommunicationTeacher( "Iftekhar Amin" ) )


class DBMS2Teacher( AbsTeacher ):

    def BusinessCommunicationStudent(self, name):
        super( name )

    def printOtherDetails(self):
        print( "I teach DBMS2" )


class DBMS2Student( AbsStudent ):

    def BusinessCommunicationStudent(self, roll, name):
        super( roll, name )

    def printOtherDetails(self):
        print("This is my one of the favourite course. Teacher teach us few time in this course but very much entertaining" );


class DBMS2Factory( Factory ):

    def bulitCourse(self):
        self.course = Course( "DBSM 2 - 504" )

    def addStudentsToCourse(self):
        self.course.addStudent( DBMS2Student( 823, "Hadi Sunney" ) )
        self.course.addStudent( DBMS2Student( 825, "Aba Kawser" ) )
        self.course.addStudent( DBMS2Student( 827, "Suravi Akhter" ) )
        self.course.addStudent( DBMS2Student( 829, "Sabik Abtahee" ) )
        self.course.addStudent( DBMS2Student( 830, "Obaidur Rahman" ) )


def main():
    while True:
        print( "enter course number :   " )
        courseNumber = int( input() )
        if courseNumber > 500 and courseNumber < 507:
            print(FactoryOFFactory().getFactory( courseNumber ))
            course = FactoryOFFactory().getFactory( courseNumber ).getCourse();
            course.printCourseDetails()


main()
