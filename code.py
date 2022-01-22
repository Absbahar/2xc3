def are_valid_groups(list_student_numbers,list_groups):
    result1 = True
    result2 = True
    for x in list_student_numbers:
        for y in list_groups:
            if y.count(x) > 1:
                result1 = False
                break
         
    for y in list_groups:
        if not (len(y) == 2 or len(y) == 3):
            result2 = False
            break
            
    if result1 == True and result2 == True:
        return True
    else
        return False

