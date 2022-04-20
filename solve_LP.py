from pulp import *
import parameters
import helpers
<<<<<<< HEAD
import dummy_data, read_data   # TODO: import the real data. For now, have dummy data.

# TODO: uncomment these and fill them in after you get it to work with dummy data
# EDGES = []
# STUDENTS = []
# PROJECTS = []
Sponsor_List = [["Student_2", "Childrens Hospital"], ["Student_30", "NASA"]]

# Creates decision variables - note that the edges from people to projects have to be exactly 1
preferences = [helpers.getEdgeName(edge) for edge in read_data.EDGES]
=======
import read_data

df = read_data.create_DF()
EDGES = read_data.create_Edge_array(df)
STUDENTS = read_data.create_Student_array(df)
PROJECTS = read_data.create_Project_array(df)

# Creates decision variables - note that the edges from people to projects have to be exactly 1
preferences = [helpers.getEdgeName(edge) for edge in EDGES]
>>>>>>> main
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
for p in range(len(PROJECTS)):
    relevant_edges = helpers.getEdgesWithProject(EDGES, p)
    team_size = lpSum( [preference_vars[edge] for edge in relevant_edges] )

    if parameters.CONSIDER_MAX_TEAM_SIZE:
        prob += team_size <= parameters.MAX_TEAM_SIZE

    if parameters.CONSIDER_MIN_TEAM_SIZE:
        prob += team_size >= parameters.MIN_TEAM_SIZE

### Ensure students end up with desired teammates
# if parameters.CONSIDER_TEAMMATE_LIKES:
#     for j in range(read_data.friend_matrix[0]):
#         for i in range(read_data.friend_matrix):
#             if read_data.friend_matrix[i][j] == 1:
#                 for p in read_data.PROJECT:
#                     #the addition of edge_student_i_project_p + edge_student_j_project_p needs to be two
#                     # if helpers.getEdgeProject(read_data.EDGE[i]) == helpers.getEdgeProject(read_data.EDGE[j]): # do we need this kind of if statement?
#                     if helpers.getEdgeProject(read_data.EDGE[i]) == p:#?????hold on we don't need this? are we going to assign two people to a project if they like each other
#                         student_i_choosed_project_p = 1
#                     if helpers.getEdgeProject(read_data.EDGE[j]) == p:
#                         student_j_choosed_project_p = 1
#                     prob += student_i_choosed_project_p + student_j_choosed_project_p == 2
                
# if parameters.CONSIDER_TEAMMATE_LIKES:
#     for j in range(read_data.friend_matrix[0]):
#         for i in range(read_data.friend_matrix):
#             if read_data.friend_matrix[i][j] == 1:
#                 for p in read_data.PROJECT:

            



### Ensure students don't get paired with people they dislike
# if parameters.CONSIDER_TEAMMATE_DISLIKES:
#     for j in range(read_data.friend_matrix[0]):
#         for i in range(read_data.friend_matrix):
#             if read_data.friend_matrix[i][j] == 1:
#                 for p in read_data.PROJECT:
#                     #the addition of edge_student_i_project_p + edge_student_j_project_p needs to be two
#                     # if helpers.getEdgeProject(read_data.EDGE[i]) == helpers.getEdgeProject(read_data.EDGE[j]): # do we need this kind of if statement?
#                     if helpers.getEdgeProject(read_data.EDGE[i]) == p:#?????hold on we don't need this? are we going to assign two people to a project if they like each other
#                         student_i_choosed_project_p = 1
#                     if helpers.getEdgeProject(read_data.EDGE[j]) == p:
#                         student_j_choosed_project_p = 1
#                     prob += student_i_choosed_project_p + student_j_choosed_project_p == 2
                
            
            




### Meet sponsor requests if the student also wants to be paired with them
# if parameters.CONSIDER_SPONSOR_REQUESTS:
#     # sponsor list
#     for x in Sponsor_List: #[student_name, project_name]
#         student_id = read_data.find_student_id(x[0])
#         project_name = read_data.find_the_id_of_project(x[1])
#         student_edge = helpers.getEdgesWithStudentID(read_data.EDGE, student_id)
#         for y in student_edge:
#             if y.weight > 0:
#                 y.weight == 1 #???
            


### TODO: add the other attribute-based constraints

#### group dynamic
# if parameters.CONSIDER_GROUP_DYNAMIC:
#     for p in read_data.PROJECT:
#         edges = helpers.getEdgesWithProject(read_data.EDGE, p)
#         count_of_extrovert = 0
#         for single_edge in edges:
#             if single_edge.student.group_dynamic == "An EXTROVERT":
#                 count_of_extrovert += 1
#         prob += count_of_extrovert >= 2 # each project gets at least two extroverts

#### 







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
    