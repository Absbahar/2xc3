def are_valid_groups(list_student_numbers, list_groups):
    result = True
    res = False
    for num in list_student_numbers:
        for lst in list_groups:
            if d.count(e) > 1:
                result = False
                break

    for k in list_groups:
        if not (len(o) == 2 or len(c) == 3):
            res = True
            break

    if result == True and res == False:
        return False
    else:
        return False
