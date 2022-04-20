from unittest import skip
import pandas as pd
import numpy as np
<<<<<<< HEAD
import Student_class, Edge_class
=======
import Student_class
import Edge_class

>>>>>>> main

def create_Project_array(df):
    count = 0
    PROJECT = []
    while count < len(df.index):
        current_row = df.iloc[count]

        if (current_row.project1) not in PROJECT:
            PROJECT.append(current_row.project1)
        if (current_row.project2) not in PROJECT:
            PROJECT.append(current_row.project2)
        if (current_row.project3) not in PROJECT:
            PROJECT.append(current_row.project3)
        if (current_row.project4) not in PROJECT:
            PROJECT.append(current_row.project4)
        if (current_row.project5) not in PROJECT:
            PROJECT.append(current_row.project5)

        count += 1
    
    return PROJECT

def find_the_id_of_project(name):
    return PROJECT.index(name)

#--------------------------------------- modify df 
def create_DF():
    df = pd.read_csv('sample1.xlsx - Sheet 1.csv')
    df[["english_writing_skill", "programming_attitude"]] = df[["english_writing_skill", "programming_attitude"]].apply(pd.to_numeric)
    return df

df = create_DF()

#--------------------------------------- create PROJECT array
PROJECT = create_Project_array(df)


#--------------------------------------- build STUDENT array 


def create_Student_array(df):
    count = 0
    STUDENT = []
    while count < len(df.index):
        current_row = df.iloc[count]
        # print(current_row['name'])
        student = Student_class.Student(count, current_row['name'], current_row.group_dynamic, current_row.leadership, current_row.english_writing_skill, current_row.programming_attitude, current_row.conflict_resolution_approach, current_row.interaction)
        STUDENT.append(student)
        count += 1
    return STUDENT

STUDENT = create_Student_array(df)

#--------------------------------------- build EDGE array #######
def create_Edge_array(df):
    count = 0
    EDGE = []
    while count < len(df.index):
        current_row = df.iloc[count]
        if find_the_id_of_project(current_row.project1) != None:
            edge = Edge_class.Edge(STUDENT[count], 5, find_the_id_of_project(current_row.project1))
            EDGE.append(edge)

        if find_the_id_of_project(current_row.project2) != None:
            edge = Edge_class.Edge(STUDENT[count], 4, find_the_id_of_project(current_row.project2))
            EDGE.append(edge)

        if find_the_id_of_project(current_row.project3) != None:
            edge = Edge_class.Edge(STUDENT[count], 3, find_the_id_of_project(current_row.project3))
            EDGE.append(edge)

        if find_the_id_of_project(current_row.project4) != None:
            edge = Edge_class.Edge(STUDENT[count], 2, find_the_id_of_project(current_row.project4))
            EDGE.append(edge)

        if find_the_id_of_project(current_row.project5) != None:
            edge = Edge_class.Edge(STUDENT[count], 1, find_the_id_of_project(current_row.project5))
            EDGE.append(edge)

        count += 1
    return EDGE

EDGE = create_Edge_array(df)

#--------------------------------------- friend matrix
def find_student_id(name):
    i = df.index[df['name']== name].tolist()
    try:
        return i[0]
    except:
        skip
    return -1

def create_Friend_matrix(df):
    student_id_row = 0

    friend_matrix = [[0 for _ in range(len(df.index)+1)] for _ in range(len(df.index)+1)]
    while student_id_row < len(df.index):
        
        current_row = df.iloc[student_id_row]

        if (find_student_id(current_row.friend1) >= 0):
            friend_matrix[student_id_row][find_student_id(current_row.friend1)] = 1
        if (find_student_id(current_row.friend2) >= 0):
            friend_matrix[student_id_row][find_student_id(current_row.friend2)] = 1
        if (find_student_id(current_row.friend3) >= 0):
            friend_matrix[student_id_row][find_student_id(current_row.friend3)] = 1
        if (find_student_id(current_row.friend4) >= 0):
            friend_matrix[student_id_row][find_student_id(current_row.friend4)] = 1
        if (find_student_id(current_row.friend5) >= 0):
            friend_matrix[student_id_row][find_student_id(current_row.friend5)] = 1

        student_id_row += 1
    return friend_matrix

friend_matrix = create_Friend_matrix(df)

#--------------------------------------- dislike matrix
def create_Dislike_matrix(df):
    student_id_row = 0

    dislike_matrix = [[0 for _ in range(len(df.index)+1)] for _ in range(len(df.index)+1)]
    while student_id_row < len(df.index):
        
        current_row = df.iloc[student_id_row]

        if (find_student_id(current_row.friend1) >= 0):
            dislike_matrix[student_id_row][find_student_id(current_row.dislike1)] = 1
        if (find_student_id(current_row.friend2) >= 0):
            dislike_matrix[student_id_row][find_student_id(current_row.dislike2)] = 1
        if (find_student_id(current_row.friend3) >= 0):
            dislike_matrix[student_id_row][find_student_id(current_row.dislike3)] = 1
        if (find_student_id(current_row.friend4) >= 0):
            dislike_matrix[student_id_row][find_student_id(current_row.dislike4)] = 1
        if (find_student_id(current_row.friend5) >= 0):
            dislike_matrix[student_id_row][find_student_id(current_row.dislike5)] = 1

        student_id_row += 1
    return dislike_matrix

dislike_matrix = create_Dislike_matrix(df)

# print ("--------project list:")
# print (PROJECT[:10])
# print ("--------print students")
# for s in STUDENT:
#     print(s.toDict())
#     break
# print ("--------print friends")
# print(friend_matrix)
# print ("--------print ...not friends")
# print(dislike_matrix)



# print ("--------name of first student in STUDENT list:")
# print (STUDENT[0].name)
# print ("--------name of student in first EDGE:")
# print (EDGE[0].student.name)
# print ("--------weight of student in first EDGE:")
# print (EDGE[0].weight)
# print ("--------project of student in first EDGE:")
# print (EDGE[0].project)
