"""
HELPER FUNCTIONS
"""
import string

def stripPunctuation(s):
    return ''.join([i for i in s if i not in string.punctuation])

def getEdgeName(edge):
    if isinstance(edge, str):
        return edge
    else:
        return 'e' + str(edge.student.ID) + str(edge.weight) + str(edge.project)

# Gets edge weight from either the edge name or the edge variables
def getEdgeWeight(edge):
    if isinstance(edge, str):
        return int(edge[2])
    else:
        return edge.weight

def getEdgeProject(edge):
    if isinstance(edge, str):
        return int(edge[3])
    else:
        return edge.project

def getEdgeFromName(edgeList, edgeName):
    for e in edgeList:
        if e.student.ID == int(edgeName[1]) and e.project == int(edgeName[3]) and e.weight == int(edgeName[2]):
            return e
    # If edge doesn't exist, return None
    return None

# Filter edges
def getEdgesWithStudentID(lstToFilter, student_id):
    if len(lstToFilter) == 0:
        return []
    # If you get list of string objects
    elif isinstance(lstToFilter[0], str):
        return [val for val in lstToFilter if val[1] == student_id]
    # If you get list of Edge objects
    else:
        return [getEdgeName(val) for val in lstToFilter if val.student.ID == student_id]

def getEdgesWithProject(lstToFilter, project):
    if len(lstToFilter) == 0:
        return []
    # If you get list of string objects
    elif isinstance(lstToFilter[0], str):
        return [val for val in lstToFilter if val[3] == project]
    # If you get list of Edge objects
    else:
        return [getEdgeName(val) for val in lstToFilter if val.project == project]
