def are_valid_groups(stdno,groups):
    for i in groups:
        for j in stdno:
            if i in j:
                return True


            