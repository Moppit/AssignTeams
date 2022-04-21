from mmap import PROT_EXEC
from pulp import *
import parameters
import helpers
import read_data

df = read_data.create_DF()
EDGES = read_data.create_Edge_array(df)
STUDENTS = read_data.create_Student_array(df)
PROJECTS = read_data.create_Project_array(df)
Sponsor_List = [["Student_1", "iSAT"], ["Student_9", "BI Inc., #1"]]

# Creates decision variables - note that the edges from people to projects have to be exactly 1
preferences = [helpers.getEdgeName(edge) for edge in EDGES]
preference_vars = LpVariable.dicts("", preferences, 0, 1, cat="Integer")

# Create the LP problem and add the decision variables
# NOTE: maximization problem because 5 = top choice, 1 = 5th choice (inverse from given form)
prob = LpProblem("Capstone_Teams_Problem", LpMaximize)

# The objective function.
prob += lpSum([helpers.getEdgeWeight(i)*preference_vars[i] for i in preferences]), "Max_Student_Happiness"

# Constraints

### Ensure students get only 1 project
if parameters.CONSIDER_PROJECT_PREFERENCES:
    for s in STUDENTS:
        relevant_edges = helpers.getEdgesWithStudentID(EDGES, s.ID)
        num_proj_assigned_per_student = lpSum([preference_vars[edge] for edge in relevant_edges])
        prob += num_proj_assigned_per_student <= parameters.PROJECTS_PER_STUDENT
        prob += num_proj_assigned_per_student >= 0

### Ensure projects are within min/max team size
for p in PROJECTS:
    relevant_edges = helpers.getEdgesWithProject(EDGES, read_data.find_the_id_of_project(p))
    team_size = lpSum( [preference_vars[edge] for edge in relevant_edges] )

    if parameters.CONSIDER_MAX_TEAM_SIZE:
        prob += team_size <= parameters.MAX_TEAM_SIZE

    if parameters.CONSIDER_MIN_TEAM_SIZE:
        prob += team_size >= parameters.MIN_TEAM_SIZE

### Ensure students end up with desired teammates
if parameters.CONSIDER_TEAMMATE_LIKES:
    for j in range(len(read_data.friend_matrix[0])):
        for i in range(len(read_data.friend_matrix)):
            if read_data.friend_matrix[i][j] == 1:
                i_project = helpers.getEdgesWithStudentID(EDGES, i)
                j_project = helpers.getEdgesWithStudentID(EDGES, j)
                for p in PROJECTS:
                    fullyfiltered = helpers.getEdgesWithProject(i_project + j_project, read_data.find_the_id_of_project(p))
                    if len(fullyfiltered) == 2:
                        prob += preference_vars[fullyfiltered[0]] - preference_vars[fullyfiltered[1]] == 0


### Ensure students don't get paired with people they dislike
if parameters.CONSIDER_TEAMMATE_DISLIKES:
    for j in range(len(read_data.dislike_matrix[0])):
        for i in range(len(read_data.dislike_matrix)):
            if read_data.dislike_matrix[i][j] == 1:
                print (i,j)
                i_project = helpers.getEdgesWithStudentID(EDGES, i)
                j_project = helpers.getEdgesWithStudentID(EDGES, j)
                for p in PROJECTS:
                    fullyfiltered = helpers.getEdgesWithProject(i_project + j_project, read_data.find_the_id_of_project(p))
                    if len(fullyfiltered) == 2:
                        prob += preference_vars[fullyfiltered[0]] + preference_vars[fullyfiltered[1]] <= 1


### Meet sponsor requests if the student also wants to be paired with them
if parameters.CONSIDER_SPONSOR_REQUESTS:
    # sponsor list
    for x in Sponsor_List: #[student_name, project_name]
        student_id = read_data.find_student_id(x[0])
        project_id = read_data.find_the_id_of_project(x[1])
        student_edge = helpers.getEdgesWithStudentID(read_data.EDGE, student_id)
        for y in student_edge:
            print ("y is: ", y)
            if helpers.getEdgeProject(y) == project_id:
                prob += preference_vars[y] == 1
            

### group dynamic: each team has at least 1 extrovert (i.e. person that talks)
if parameters.CONSIDER_GROUP_DYNAMIC:
    for p in PROJECTS:
        relevant_edges = helpers.getEdgesWithProject(EDGES, read_data.find_the_id_of_project(p))
        extrovert_count = lpSum( [helpers.getEdgeFromName(EDGES, edge).student.isExtrovert()*preference_vars[edge] for edge in relevant_edges] )
        prob += extrovert_count >= parameters.NUM_EXTROVERTS








prob.writeLP("CapstoneTeamsProblem.lp")
prob.solve()
# TODO: add a print pretty option vs. print raw option
print('\n\n------------------ FINAL COMPUTATION ------------------')
print("Status:", LpStatus[prob.status])
print()
final_edges = []
for v in prob.variables():
    if v.varValue == 1:
        # print(v.name, "=", v.varValue)
        varName = v.name[1:]
        edge = helpers.getEdgeFromName(EDGES, varName)
        final_edges.append(edge)

# Print Pretty
if LpStatus[prob.status] == 'Optimal':
    # Display all edges
    for i in range(len(PROJECTS)):
        print(PROJECTS[i], ':', [edge for edge in helpers.getEdgesWithProject(final_edges, i)])
    