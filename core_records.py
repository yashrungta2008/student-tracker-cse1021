import input_guards
def add_student(students):
    print("register new student")
    s_id=input_guards.get_int_input("enter student id number:")
    if s_id in students:
        print("error: id already exists in system")
        return
    name=input("enter student name:").strip()
    if name=="":
        print("name cannot be blank")
        return
    total_cls=input_guards.get_int_input("total number of classes:")
    if total_cls<0:
        print("classes cannot be negative")
        return
    att_cls=input_guards.get_int_input("number of classes attended:")
    if att_cls<0 or att_cls>total_cls:
        print("invalid attendance numbers entered")
        return
    print("enter the 3 assignment marks:")
    marks=[]
    for x in range(3):
        score=input_guards.get_float_input(f"assignment {x+1}:")
        marks.append(score)
    students[s_id]={'name':name,'total':total_cls,'present':att_cls,'marks':marks}
    print("saved student"+ name +" successfully")
def show_all_students(students):
    print("listing all records")
    if len(students)==0:
        print("no records to display")
        return
    for k in students:
        data=students[k]
        print(f"ID:{k}|Name:{data['name']}")
        print(f" Marks:{data['marks']}")
        print(f" Attendance:{data['present']}/{data['total']}")
def delete_student(students):
    print("delete record")
    target=input_guards.get_int_input("enter student id to delete:")
    if target in students:
        del students[target]
        print("successfully removed student from database")
    else:
        print("student id not found")
