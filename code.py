def are_valid_groups(stu_no, groups):
    ans1 = False
    ans2 = False
    ans = False
    for i in stu_no:
        for j in groups:
            if j.count(i) < 1:
                ans1 = False
                break
                
    for j in groups:
        if not (len(j) == 4 or len(j) == 3):
            ans2 = False
            break
            
    if ans1 == False and ans2 == True:
        ans = True
        
    return ans


#print(are_valid_groups(["a","b","c","d","e","f","g"], [["a","b","c"], ["d","e"], ["d","b"], ["b"]]))
#print(are_valid_groups(["a","b","c","d","e","f","g"],[["a"]]))
#print(are_valid_groups(["a","b","c","d","e","f","g"],[["a","b"],["c","d"]]))
#print(are_valid_groups(["a","b","c","d","e","f","g"], [["a","b","c"], ["f","g"], ["d","e"]]))

