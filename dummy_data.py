"""
DUMMY DATA

This data has a small set of students and projects to see how matching them would work.
This should be removed from solve_LP.py when the real data is available.
It might not be a bad idea to keep this dummy data around for testing though, 
especially for new features.

Students                            Projects

1.  [1, 3, 4, 5, 6]                 1. 

2.  [4, 2, 5, 1]                    2.

3.  [2, 6, 1, 5]                    3. 

4.  [3, 4, 6, 5]                    4. 

                                    5. 
                    
                                    6.
"""

EDGES = []
STUDENTS = []
PROJECTS = ['Zayo', 'NASA', 'L3Harris', 'CU English', 'iSAT', 'UCAR']

class Student:
    def __init__(self, id):
        self.ID = id

class Edge:
    def __init__(self, s, w, p):
        self.student = s
        self.weight = w
        self.project = p

# Student 1
s1 = Student(1)
STUDENTS.append(s1)
EDGES.append(Edge(s1, 5, 0))
EDGES.append(Edge(s1, 4, 2))
EDGES.append(Edge(s1, 3, 3))
EDGES.append(Edge(s1, 2, 4))
EDGES.append(Edge(s1, 1, 5))

# Student 2
s2 = Student(2)
STUDENTS.append(s2)
EDGES.append(Edge(s2, 5, 3))
EDGES.append(Edge(s2, 4, 1))
EDGES.append(Edge(s2, 3, 4))
EDGES.append(Edge(s2, 2, 0))

# Student 3
s3 = Student(3)
STUDENTS.append(s3)
EDGES.append(Edge(s3, 5, 1))
EDGES.append(Edge(s3, 4, 5))
EDGES.append(Edge(s3, 3, 0))
EDGES.append(Edge(s3, 2, 4))

# Student 4
s4 = Student(4)
STUDENTS.append(s4)
EDGES.append(Edge(s4, 5, 2))
EDGES.append(Edge(s4, 4, 3))
EDGES.append(Edge(s4, 3, 5))
EDGES.append(Edge(s4, 2, 4))