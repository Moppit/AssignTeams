from pulp import *
import parameters
import helpers
import read_data

df = read_data.create_DF()
EDGES = read_data.create_Edge_array(df)
STUDENTS = read_data.create_Student_array(df)
PROJECTS = read_data.create_Project_array(df)

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
for p in range(len(PROJECTS)):
    relevant_edges = helpers.getEdgesWithProject(EDGES, p)
    team_size = lpSum( [preference_vars[edge] for edge in relevant_edges] )

    if parameters.CONSIDER_MAX_TEAM_SIZE:
        prob += team_size <= parameters.MAX_TEAM_SIZE

    if parameters.CONSIDER_MIN_TEAM_SIZE:
        prob += team_size >= parameters.MIN_TEAM_SIZE

### Ensure students end up with desired teammates

### Ensure students don't get paired with people they dislike

### Meet sponsor requests if the student also wants to be paired with them

### TODO: add the other attribute-based constraints

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
    