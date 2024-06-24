students = ["hari" , "rajini" ,  "sai"]
#print(students[0])
#print(students[1])
#print(students[2]) #better code writing
#for student in students:
    #print(student)
#for i in range(len(students)):
    #print(students[i]) 
    #print(i+1,students[i] )
    #===============Dictionaries==========
students = {
    "hari": "bolleboyana",
    "kiran": "kotari",
    "rajini": "bolleboyana",
}
#print(students["hari"])
#print(students["kiran"])
#print(students["rajini"])
for student in students:
    #print(student, students[student])
    print(student, students[student], sep=",")

