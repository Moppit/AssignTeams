"""
HELPER FUNCTIONS
"""

def getEdgeName(edge):
    return 'e' + str(edge.student.ID) + str(edge.weight) + str(edge.project)

# Gets edge weight from either the edge name or the edge variables
def getEdgeWeight(edge):
    if isinstance(edge, str):
        return int(edge[2])
    else:
        return edge.weight

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