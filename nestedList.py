"""
this program prints the name(s) of student(s) with the second lowest score for student whose name and scores are given.
"""
if __name__ == '__main__':
    # define an empty list for student name and score
    name_list , score_list = [],[]
    # get the number of students whose records are to be inserted
    n = int(input())

    # get the name of each student and their respective scores
    for i in range(n):
        name = input()
        score = float(input())
        name_list.append(name)
        score_list.append(score)

    students_name_score= sorted([ [name,score] for name,score in zip(name_list,score_list)])
    print(students_name_score)

    #convert score list to set to remove duplicate
    score_list2 = set(score_list)
    print(score_list2)
    # find the first minimum score
    first_min = min(score_list2)
    print(first_min)

    #return the score list back to a list
    score_list = list(score_list2)
    print(score_list)
    # the remove the first minimun from the list
    for i in score_list:
        if i == first_min:
            score_list.remove(i)
    # find the next minimum score
    next_min = min(score_list)
    print(next_min)
    for student_record in students_name_score:
        # check the if the next_min score is equal to the student's score
        if next_min == student_record[1]: 
            print('second lowest score is:{}'.format(student_record[0]))