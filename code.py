
def are_valid_groups(list_student_numbers, list_groups):
    result = False
    for x in list_student_numbers:
        for y in list_groups:
            if x in y:
                result = True
    return result
