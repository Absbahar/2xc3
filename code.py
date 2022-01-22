def are_valid_groups():
    for x in list_student_numbers:
        for y in list_groups:
            if x in y:
                result = True
    return result