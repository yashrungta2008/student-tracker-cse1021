def get_average(m_list):
    if not m_list:
        return 0.0
    sum_val=0.0
    for m in m_list:
        sum_val+=m
    return sum_val/len(m_list)
def find_top_student(students):
    if not students:
        print("registry is empty")
        return
    best_id=-1
    top_avg=-1.0
    for idx in students:
        avg=get_average(students[idx]['marks'])
        if avg>top_avg:
            top_avg=avg
            best_id=idx
    print("Highest marks belongs to:"+ students[best_id]['name'])
    print(f"Average:{top_avg:.2f}")
def sort_students(students):
    print("sorting students by performance")
    if not students:
        print("nothing to sort")
        return
    s_list=[]
    for sid in students:
        avg=get_average(students[sid]['marks'])
        s_list.append({'id':sid,'name':students[sid]['name'],'avg':avg})
    length=len(s_list)
    for i in range(length):
        max_pos=i
        for j in range(i+1,length):
            if s_list[j]['avg']>s_list[max_pos]['avg']:
                max_pos=j
        temp=s_list[i]
        s_list[i]=s_list[max_pos]
        s_list[max_pos]=temp
    print("Rank|ID|Name|Average")
    for r, s in enumerate(s_list):
        print(f"{r+1}|{s['id']}|{s['name']}|{s['avg']:.2f}")
