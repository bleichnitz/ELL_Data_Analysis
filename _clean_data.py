def filter_for_student(student,list):
    content = False
    student_data = []
    for i in range(0,len(list)):
        if student == list[i][0]:
            student_data.append(list[i])
            content = True
    if content is True:
        return student_data
    else:
        return False


def check_student(student, check_list):
    for row in check_list:
        if student == row[0]:
            return True
    return False


def clean_SIS_ell_list(data):
    col_student_num = 84  # column CF
    col_surname = 91  # column CN
    col_preferred_name = 82  # column CE
    col_sex = 88  # column CK
    col_language_one = 16  # column Q
    col_language_two = 17  # column R
    col_grade = 13  # column N

    ell_list = []
    current_student_num = 0
    previous_student_num = 0

    for row in data.values:
        if row[col_student_num] is not None:
            current_student_num = (row[col_student_num])
            if current_student_num is not previous_student_num:
                current_student = []
                current_student.append(row[col_student_num])
                current_student.append(row[col_surname])
                current_student.append(row[col_preferred_name])
                current_student.append(row[col_sex])
                current_student.append(row[col_grade])
                current_student.append(row[col_language_one])
                current_student.append(row[col_language_two])

                previous_student_num = current_student_num
            ell_list.append(current_student)
    ell_list.pop(0)  #remove header row

    #print("")
    #for row in ell_list:
    #    print(row)
    #print("")
    print(f"\tSIS ELL List > number of students: {len(ell_list)}")
    return ell_list


def clean_ell_list(data):
    wd_s_num = 0  # column A
    wd_l_name = 1  # column B
    wd_f_name = 2  # column C
    wd_sex = 3  # column D
    wd_grade = 4  # column G
    wd_language_one = 5  # column E
    wd_language_two = 6  # column F

    clean_list = []
    for row in data.values:
        if row[wd_s_num] is not None:
            clean_list.append(row)
    clean_list.pop(0)
    # print("")
    # for row in clean_list:
    #    print(row)
    # print(row)
    print(f"\tWORKING ELL List > number of students: {len(clean_list)}")
    return clean_list


def add_remove_students(working_list, sis_list):

    add_students = []
    remove_students = []
    print("")
    print("REMOVE LIST")
    for row in working_list:
        student_id = row[0]
        status = check_student(student=student_id, check_list=sis_list)
        if status is False:
            remove_students.append(row)
            print(f"\t {student_id} -- {status}")
    print(f"# students to remove: {len(remove_students)}")
    print("")
    print("ADD LIST")
    for row in sis_list:
        student_id = row[0]
        status = check_student(student=student_id, check_list=working_list)
        if status is False:
            add_students.append((row))
            print(f"\t {student_id} -- {status}")
    print(f"# students to add: {len(add_students)}")
    balance = len(working_list) + len(add_students) - len(remove_students)
    print(f"{len(working_list)} + {len(add_students)} - {len(remove_students)} = {len(sis_list)} (B = {balance})")


def clean_grade_summary(grade_data, ell_list):
    mgs_student_number = 118
    mgs_col_MT_average = 45
    mgs_col_F_average = 52
    mgs_course_grade = 95
    mgs_course_code = 64
    mgs_absences = 75
    mgs_course_teacher = 125

    grade_list = []

    for row in grade_data.values:
        row_data = []
        current_student = row[mgs_student_number]
        status = check_student(student=current_student, check_list=ell_list)
        if row[mgs_student_number] is not None and status == True:
            row_data.append(row[mgs_student_number])
            row_data.append(row[mgs_col_MT_average])
            row_data.append(row[mgs_col_F_average])
            row_data.append(row[mgs_course_grade])
            row_data.append(row[mgs_course_code])
            row_data.append(row[mgs_absences])
            row_data.append(row[mgs_course_teacher])
            #print(row_data)
            grade_list.append(row_data)

    grade_list.pop(0)

    final_list = []
    for s in range(0,len(ell_list)):
        current_student_number = ell_list[s][0]
        current_student_data = filter_for_student(student=current_student_number, list=grade_list)
        if current_student_data is not False:
            final_list.append(current_student_data)

    for row in final_list:
        print(row)
    print(len(final_list))

    return final_list
