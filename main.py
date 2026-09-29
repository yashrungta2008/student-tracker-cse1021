import sys
import input_guards
import core_records
import grades_analyzer
import attendance_manager
def run_app():
    students_db={}
    while True:
        print("STUDENT RECORD SYSTEM")
        print("1.add new student")
        print("2.view all students")
        print("3.delete student record")
        print("4.rank students by grades")
        print("5.find top performer")
        print("6.check attendance alerts")
        print("7.exit application")
        opt=input_guards.get_int_input("choose option(1-7): ")
        if opt==1:
            core_records.add_student(students_db)
        elif opt==2:
            core_records.show_all_students(students_db)
        elif opt==3:
            core_records.delete_student(students_db)
        elif opt==4:
            grades_analyzer.sort_students(students_db)
        elif opt==5:
            grades_analyzer.find_top_student(students_db)
        elif opt==6:
            attendance_manager.check_low_attendance(students_db)
        elif opt==7:
            print("closing program now")
            sys.exit(0)
        else:
            print("invalid selection number, pick 1 to 7")
if __name__=='__main__':
    run_app()
