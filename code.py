def are_valid_groups(stu_no, groups):
    ans1 = True
    ans2 = True
    ans = False
    for i in stu_no:
        for j in groups:
            if j.count(i) > 1:
                ans1 = False
                break
                
    for j in groups:
        if not (len(j) == 2 or len(j) == 3):
            ans2 = False
            break
            
    if ans1 == False and ans2 == True:
        ans = True
        
    return ans


