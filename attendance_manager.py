def check_low_attendance(students):
    print("low attendance alerts(<75%)")
    if not students:
        print("no student records found")
        return
    has_issue=False
    for sid in students:
        info=students[sid]
        if info['total']>0:
            pct=(float(info['present'])/float(info['total']))*100.0
        else:
            pct=0.0
        if pct<75.0:
            print(f"alert:{info['name']} (ID: {sid}) has only {pct:.1f}% attendance")
            has_issue=True
    if not has_issue:
        print("all students are clear and above 75%")
