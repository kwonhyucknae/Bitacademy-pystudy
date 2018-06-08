students=[
    {
        "name":"Kim",   
        "kor":80,
        "eng":90,
        "math":80
    },
    {
        "name":"Lee",
        "kor":90,
        "eng":85,
        "math":85
    }
]

for student in students:
    total = student.get('kor') + student.get('eng') + student.get('math')
    average=total/3
    student['total']=total
    student['average']=average

print(students)




'''
print(students[0]['name'])
total=students[0]['kor']+students[0]['eng']+students[0]['math']+students[1]['kor']+students[1]['eng']+students[1]['math']
average=total/2
d={"total":total,"average":average}
print(d)
'''