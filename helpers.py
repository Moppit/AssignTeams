"""
HELPER FUNCTIONS
"""
import string

def getEdgeName(edge):
    if isinstance(edge, str):
        return edge
    else:
        return str(edge.student.ID) + '_' + str(edge.weight) + '_' + str(edge.project)

# Gets edge weight from either the edge name or the edge variables
def getEdgeWeight(edge):
    if isinstance(edge, str):
        arr = edge.split('_')
        return int(arr[1])
    else:
        return edge.weight

def getEdgeStudentID(edge):
    if isinstance(edge, str):
        arr = edge.split('_')
        return int(arr[0])
    else:
        return edge.student.ID


def getEdgeProject(edge):
    if isinstance(edge, str):
        arr = edge.split('_')
        return int(arr[2])
    else:
        return edge.project

def getEdgeFromName(edgeList, edgeName):
    arr = edgeName.split('_')
    id = int(arr[0])
    w = int(arr[1])
    proj = int(arr[2])
    for e in edgeList:
        if e.student.ID == id and e.project == proj and e.weight == w:
            return e
    # If edge doesn't exist, return None
    return None

# Filter edges
# @return: array of strings
def getEdgesWithStudentID(lstToFilter, student_id):
    if len(lstToFilter) == 0:
        return []
    # If you get list of string objects
    elif isinstance(lstToFilter[0], str):
        
        return [val for val in lstToFilter if getEdgeStudentID(val) == student_id]
    # If you get list of Edge objects
    else:
        return [getEdgeName(val) for val in lstToFilter if val.student.ID == student_id]

def getEdgesWithProject(lstToFilter, project):
    if len(lstToFilter) == 0:
        return []
    # If you get list of string objects
    elif isinstance(lstToFilter[0], str):
        return [val for val in lstToFilter if getEdgeProject(val) == project]
    # If you get list of Edge objects
    else:
        return [getEdgeName(val) for val in lstToFilter if val.project == project]
