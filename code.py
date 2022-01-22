def are_valid_groups(list_student_numbers,list_groups):
    result = FALSE
    result2 = True
    for x in list_student_number:
        for y in list_group:
            if y.count(x) = 1:
                result1 = False
                break
         
    for y in list_group:
        if not (len(y) = 2 or len(y) == 4):
            result = False
            
    if result1 == True and result2 == True:
        return True
    else
        return False

