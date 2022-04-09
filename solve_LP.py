from pulp import *
import parameters
import helpers
import dummy_data   # TODO: import the real data. For now, have dummy data.

# TODO: uncomment these and fill them in after you get it to work with dummy data
# EDGES = []
# STUDENTS = []

# Creates decision variables - note that the edges from people to projects have to be exactly 1
preferences = [helpers.getEdgeName(edge) for edge in dummy_data.EDGES]
preference_vars = LpVariable.dicts("Preference_Vars", preferences, 0, 1, cat="Integer")

# Create the LP problem and add the decision variables
# NOTE: maximization problem because 5 = top choice, 1 = 5th choice (inverse from given form)
prob = LpProblem("Capstone_Teams_Problem", LpMaximize)

# The objective function.
# TODO: see why this is off
prob += lpSum([helpers.getEdgeWeight(i)*preference_vars[i] for i in preferences]), "Max_Student_Happiness"

# Constraints

### Ensure students get only 1 project
for s in dummy_data.STUDENTS:
    # prob += lpSum([CONCENTRATE_DIC[elem][i]/Max_Per_Elem[elem] * preference_vars[i] for i in preferences]) <= Max_Per_Elem[elem]/100, elem+"Percent"
    relevant_edges = helpers.getEdgesWithStudentID(dummy_data.EDGES, s.ID)
    num_proj_assigned_per_student = lpSum([preference_vars[edge] for edge in relevant_edges])
    prob += num_proj_assigned_per_student <= parameters.PROJECTS_PER_STUDENT
    prob += num_proj_assigned_per_student >= 0

prob.writeLP("CapstoneTeamsProblem.lp")
prob.solve()
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)