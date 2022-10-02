
if __name__ == '__main__':
    science_student = {'Alex','Dany','Xavi','Roni','Silva'}
    maths_student = {'Cook','Bell','Alex','Dany'}

    # union
    # combine both set
    list_of_all_students = science_student.union(maths_student)
    print(f' list_of_all_students {list_of_all_students}')

    list_who_entrolled_only_in_science = science_student.difference(maths_student)
    print(f'list_who_entrolled_only_in_science {list_who_entrolled_only_in_science}')

    list_who_entrolled_only_in_maths =maths_student.difference(science_student)
    print(f'list_who_entrolled_only_in_maths {list_who_entrolled_only_in_maths}')

    list_who_entrolled_only_one_subject  = maths_student.symmetric_difference(science_student)
    print(f'list_who_entrolled_only_one_subject {list_who_entrolled_only_one_subject}')

    list_who_entrolled_both_subjects = maths_student.intersection(science_student)
    print(f'list_who_entrolled_both_subjects {list_who_entrolled_both_subjects}')

