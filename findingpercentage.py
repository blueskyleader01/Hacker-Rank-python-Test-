"""
this program use dictionary to find the percentage of student records
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    print(student_marks)
    query_name = input()
    for key, value in student_marks.items():
        if query_name == key:
            percent = sum(value)/len(value)
            print ("{:.2f}".format(percent))