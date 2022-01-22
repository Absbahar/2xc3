def are_valid_groups(list_student_numbers, list_groups):
    result = True
    res = True
    for num in list_student_numbers:
        for lst in list_groups:
            if lst.count(num) > 1:
                result = False
                break

    for lst in list_groups:
        if not (len(lst) == 2 or len(lst) == 3):
            res = False
            break

    if result == True and res == True:
        return True
    else:
        return False
